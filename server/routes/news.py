"""News API routes for fetching recent articles by topic.

This module exposes endpoints for retrieving news items via the Perplexity service.
"""

import logging
from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from server.config import getConfig
from server.models import NewsItem, TopicRequest
from server.services.perplexity_client import PerplexityClient


logger = logging.getLogger(__name__)


class TopicNewsResponse(BaseModel):
    """Response payload containing news items for a single topic."""
    
    topic: str
    items: List[NewsItem]


router = APIRouter(prefix="/api", tags=["news"])


@router.post("/get_news", response_model=List[TopicNewsResponse])
def get_news(request: TopicRequest) -> List[TopicNewsResponse]:
    """Fetch recent news articles for the specified topics.
    
    Args:
        request: TopicRequest containing list of topics to query
    
    Returns:
        List of TopicNewsResponse, one per requested topic
    
    Raises:
        HTTPException: 500 if service layer fails
    """
    try:
        config = getConfig()
        perplexity_client = PerplexityClient(api_key=config.perplexityApiKey)
        
        results: List[TopicNewsResponse] = []
        
        for topic in request.topics:
            logger.info("Fetching news for topic: %s", topic)
            news_items = perplexity_client.search_latest(topic, max_results=5)
            results.append(TopicNewsResponse(topic=topic, items=news_items))
        
        logger.info("Successfully fetched news for %d topics", len(request.topics))
        return results
        
    except RuntimeError as error:
        logger.error("Configuration error: %s", error)
        raise HTTPException(status_code=500, detail="Server configuration error") from error
    except Exception as error:
        logger.error("Unexpected error in get_news endpoint: %s", error)
        raise HTTPException(status_code=500, detail="Internal server error") from error

