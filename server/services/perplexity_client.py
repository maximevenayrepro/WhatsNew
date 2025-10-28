"""Perplexity API client wrapper for searching recent news articles.

This module provides a stable interface for querying news via the Perplexity API.
"""

import logging
import re
from typing import Optional

import requests

from server.models import NewsItem


logger = logging.getLogger(__name__)


class PerplexityClient:
    """Client for searching recent news articles via Perplexity API."""
    
    API_URL = "https://api.perplexity.ai/chat/completions"
    DEFAULT_MODEL = "sonar"
    REQUEST_TIMEOUT = 30.0  # seconds
    
    def __init__(self, api_key: str) -> None:
        """Initialize the Perplexity client with an API key.
        
        Args:
            api_key: Perplexity API key for authentication
        """
        self.api_key = api_key
    
    def search_latest(self, topic: str, max_results: int) -> list[NewsItem]:
        """Search for the most recent news articles on a given topic.
        
        Makes a real API call to Perplexity to fetch recent news (last 24 hours).
        
        Args:
            topic: The topic or keyword to search for (e.g., "technology", "politics")
            max_results: Maximum number of results to return (capped at 5)
        
        Returns:
            List of NewsItem objects parsed from Perplexity API response.
            Returns empty list on error.
        """
        # Build the query
        query = f"Latest news about {topic} in the past 24 hours. Provide up to {max_results} news items with title, brief summary, and source URL."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        
        payload = {
            "model": self.DEFAULT_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that extracts recent news. "
                        "Return results in a structured format: each news item on a new line with "
                        "TITLE: <title>, SNIPPET: <snippet>, URL: <url>"
                    ),
                },
                {
                    "role": "user",
                    "content": query,
                },
            ],
        }
        
        try:
            response = requests.post(
                self.API_URL,
                headers=headers,
                json=payload,
                timeout=self.REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            
            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Parse the structured response into NewsItem objects
            news_items = self._parse_response(content, topic, max_results)
            
            logger.info("Successfully fetched %d news items for topic '%s'", len(news_items), topic)
            return news_items
            
        except requests.exceptions.Timeout:
            logger.error("Perplexity API request timed out after %s seconds", self.REQUEST_TIMEOUT)
            return []
        except requests.exceptions.RequestException as error:
            logger.error("Perplexity API request failed: %s", str(error))
            return []
        except Exception as error:
            logger.error("Unexpected error during Perplexity search: %s", str(error))
            return []
    
    def _parse_response(self, content: str, topic: str, max_results: int) -> list[NewsItem]:
        """Parse Perplexity response content into NewsItem objects.
        
        Args:
            content: Raw text response from Perplexity API
            topic: Original search topic
            max_results: Maximum number of items to return
        
        Returns:
            List of parsed NewsItem objects
        """
        news_items: list[NewsItem] = []
        
        # Try to extract structured data using regex patterns
        # Pattern: TITLE: ... SNIPPET: ... URL: ...
        pattern = r"TITLE:\s*([^\n]+).*?SNIPPET:\s*([^\n]+).*?URL:\s*([^\s\n]+)"
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        
        for match in matches[:max_results]:
            title, snippet, url = match
            news_items.append(
                NewsItem(
                    title=title.strip(),
                    snippet=snippet.strip(),
                    url=url.strip(),
                    topic=topic,
                )
            )
        
        # Fallback: if no structured matches, try to extract URLs and create basic items
        if not news_items:
            url_pattern = r"https?://[^\s\)]+"
            urls = re.findall(url_pattern, content)
            
            if urls:
                # Create basic news items from found URLs
                for url in urls[:max_results]:
                    news_items.append(
                        NewsItem(
                            title=f"News about {topic}",
                            snippet=content[:200] if len(content) > 200 else content,
                            url=url,
                            topic=topic,
                        )
                    )
        
        return news_items

