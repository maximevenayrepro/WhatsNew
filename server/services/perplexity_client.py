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
        query = f"Latest news about {topic} in the past 7 days. Provide up to {max_results} news items with title, brief summary, and source URL."
        
        logger.info("Searching for topic '%s'", topic)
        
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
                        "You are a news aggregator. For each news item, you MUST provide:\n"
                        "1. TITLE: The article headline\n"
                        "2. SNIPPET: A brief 1-2 sentence summary\n"
                        "3. URL: The full web link to the article\n\n"
                        "Format each item EXACTLY like this:\n"
                        "TITLE: [article title]\n"
                        "SNIPPET: [summary]\n"
                        "URL: [full https URL]\n\n"
                        "Always include real URLs from reputable news sources."
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
            
            logger.info("Perplexity response for topic '%s': %s", topic, content[:200])
            
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
        seen_urls: set[str] = set()  # Track URLs to avoid duplicates
        
        logger.info("Parsing response for topic '%s', content length: %d", topic, len(content))
        
        # Try to extract structured data using regex patterns
        # Pattern: TITLE: ... SNIPPET: ... URL: ...
        pattern = r"TITLE:\s*([^\n]+).*?SNIPPET:\s*([^\n]+).*?URL:\s*([^\s\n]+)"
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        
        logger.info("Found %d structured matches for topic '%s'", len(matches), topic)
        
        for match in matches:
            if len(news_items) >= max_results:
                break
                
            title, snippet, url = match
            url_clean = url.strip()
            
            # Skip duplicates
            if url_clean in seen_urls:
                logger.debug("Skipping duplicate URL for topic '%s': %s", topic, url_clean)
                continue
            
            seen_urls.add(url_clean)
            news_items.append(
                NewsItem(
                    title=title.strip(),
                    snippet=snippet.strip(),
                    url=url_clean,
                    topic=topic,
                )
            )
        
        # Fallback: if no structured matches, try to extract URLs and create basic items
        if not news_items:
            logger.warning("No structured matches found for topic '%s', trying URL extraction fallback", topic)
            url_pattern = r"https?://[^\s\)]+"
            urls = re.findall(url_pattern, content)
            
            logger.info("Found %d URLs in fallback for topic '%s'", len(urls), topic)
            
            if urls:
                # Create basic news items from found URLs (with deduplication)
                for url in urls:
                    if len(news_items) >= max_results:
                        break
                    
                    url_clean = url.strip()
                    if url_clean not in seen_urls:
                        seen_urls.add(url_clean)
                        news_items.append(
                            NewsItem(
                                title=f"News about {topic}",
                                snippet=content[:200] if len(content) > 200 else content,
                                url=url_clean,
                                topic=topic,
                            )
                        )
            else:
                logger.warning("No URLs found in response for topic '%s'. Response: %s", topic, content[:500])
        
        logger.info("Returning %d unique news items for topic '%s'", len(news_items), topic)
        return news_items

