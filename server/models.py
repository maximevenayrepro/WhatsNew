"""Data models for news API request and response payloads.

This module defines Pydantic schemas used across the news service endpoints.
"""

from pydantic import BaseModel, Field


class NewsItem(BaseModel):
    """Represents a single news article with title, snippet, URL, and topic."""
    
    title: str = Field(..., min_length=1, description="Article headline")
    snippet: str = Field(..., min_length=1, description="Article summary or excerpt")
    url: str = Field(..., min_length=1, description="Full URL to the article")
    topic: str = Field(..., min_length=1, description="Topic category for this article")


class TopicRequest(BaseModel):
    """Request payload for fetching news by one or more topics."""
    
    topics: list[str] = Field(..., min_length=1, description="List of topics to query")

