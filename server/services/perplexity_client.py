"""Perplexity API client wrapper for searching recent news articles.

This module provides a stable interface for querying news. The current implementation
returns fake deterministic data to enable frontend development before integrating
the real Perplexity API.
"""

from server.models import NewsItem


class PerplexityClient:
    """Client for searching recent news articles via Perplexity API.
    
    Current implementation returns fake data for development purposes.
    Real API integration will replace this in a future task.
    """
    
    def search_latest(self, topic: str, max_results: int) -> list[NewsItem]:
        """Search for the most recent news articles on a given topic.
        
        Args:
            topic: The topic or keyword to search for (e.g., "technology", "politics")
            max_results: Maximum number of results to return (currently capped at 3)
        
        Returns:
            List of NewsItem objects with fake deterministic data.
            Returns 1-3 items depending on the topic and max_results.
        """
        fake_data_map: dict[str, list[NewsItem]] = {
            "technology": [
                NewsItem(
                    title="AI Breakthrough in Natural Language Processing",
                    snippet="Researchers announce significant improvements in LLM efficiency and accuracy.",
                    url="https://example.com/ai-breakthrough",
                    topic="technology",
                ),
                NewsItem(
                    title="New Quantum Computing Milestone Reached",
                    snippet="Scientists demonstrate stable qubits at room temperature for the first time.",
                    url="https://example.com/quantum-milestone",
                    topic="technology",
                ),
            ],
            "politics": [
                NewsItem(
                    title="Major Policy Reform Announced",
                    snippet="Government unveils comprehensive plan for infrastructure modernization.",
                    url="https://example.com/policy-reform",
                    topic="politics",
                ),
            ],
            "sports": [
                NewsItem(
                    title="Championship Finals Set for Next Week",
                    snippet="Two top teams to compete in highly anticipated season finale.",
                    url="https://example.com/championship-finals",
                    topic="sports",
                ),
                NewsItem(
                    title="Record-Breaking Performance in Athletics",
                    snippet="Athlete shatters world record in 100m sprint with stunning time.",
                    url="https://example.com/record-breaking",
                    topic="sports",
                ),
                NewsItem(
                    title="Major League Announces Expansion Plans",
                    snippet="League to add two new teams in major metropolitan areas starting next season.",
                    url="https://example.com/league-expansion",
                    topic="sports",
                ),
            ],
        }
        
        # Default fallback for unknown topics
        default_items: list[NewsItem] = [
            NewsItem(
                title=f"Latest Updates on {topic.capitalize()}",
                snippet=f"Stay informed with the most recent developments in {topic}.",
                url=f"https://example.com/{topic.lower().replace(' ', '-')}",
                topic=topic,
            ),
        ]
        
        items: list[NewsItem] = fake_data_map.get(topic.lower(), default_items)
        
        # Respect max_results limit
        return items[:max_results]

