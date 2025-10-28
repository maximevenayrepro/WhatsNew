# WhatsNew - Architecture & Technical Documentation

This document provides technical details about the project's architecture, data models, services, and implementation patterns.

## Architecture Overview

### Technology Stack

- **Backend Framework**: FastAPI
- **Language**: Python 3.11+
- **Frontend**: Vanilla HTML/CSS/JavaScript (ES6)
- **External APIs**: Perplexity AI for news search

### Architectural Patterns

- REST API design
- Service layer for external API integration
- Simple MVC separation (no framework)
- Environment-based configuration
- CORS restricted to localhost only

## Data Models

The backend uses Pydantic models for type-safe request and response payloads:

### NewsItem

Represents a single news article:

```python
{
    "title": str,        # Article title
    "snippet": str,      # Brief summary or excerpt
    "url": str,         # Link to full article
    "topic": str        # Associated topic/category
}
```

Validation rules:
- All fields are required and must be non-empty strings
- URLs should be valid HTTP/HTTPS links

### TopicRequest

Request payload for fetching news:

```python
{
    "topics": list[str]  # List of topics to query
}
```

Validation rules:
- Must contain at least one topic
- Each topic must be a non-empty string

**Location**: `server/models.py`

## Services

### Perplexity Client

The `PerplexityClient` service provides a stable interface for searching recent news articles via the Perplexity API.

**Location**: `server/services/perplexity_client.py`

**Implementation**: Integrates with the Perplexity API to fetch real-time news data from the last 24 hours, limited to 5 results per topic.

#### Features

- **Real-time news search**: Queries Perplexity API for recent articles (last 24 hours)
- **Structured parsing**: Extracts title, snippet, and URL from API responses
- **Error handling**: Graceful fallback on API errors with logging
- **Timeout protection**: 30-second timeout for API requests
- **Model**: Uses Perplexity's `sonar` model for online search

#### Usage Example

```python
from server.config import getConfig
from server.services.perplexity_client import PerplexityClient

config = getConfig()
client = PerplexityClient(api_key=config.perplexityApiKey)
results = client.search_latest(topic="technology", max_results=5)
# Returns a list of NewsItem objects with real data
```

#### Methods

- `__init__(api_key: str) -> None`
  - Initializes the client with a Perplexity API key
  
- `search_latest(topic: str, max_results: int) -> list[NewsItem]`
  - Searches for recent news articles about the given topic
  - Returns up to `max_results` items (capped at 5)
  - Returns empty list on error
  - Query format: "Latest news about {topic} in the past 24 hours"

## API Endpoints

### Current Endpoints

- `GET /` — Returns plain text `Hello World` (`text/plain`)
- `GET /api/health` — Returns JSON `{ "status": "ok" }`

### Planned Endpoints

- `POST /api/get_news` — Accepts `TopicRequest`, returns news items grouped by topic
- `POST /api/set_key` — Stores and validates Perplexity API key (server-side only)

## Security Considerations

- **API Key Storage**: Perplexity API key is stored server-side only and never exposed to the client
- **CORS**: Restricted to localhost for local development
- **Secrets**: Never logged or included in error messages
- **Configuration**: `config/local_settings.json` is gitignored

## Configuration

Configuration is loaded from `config/local_settings.json`:

```json
{
  "perplexity_api_key": "pplx-YOUR-API-KEY-HERE"
}
```

**Configuration loading**: Handled by `server/config.py` and `server/startup.py`

## File Structure

```
WhatsNew/
├── server/
│   ├── main.py              # FastAPI app entry point
│   ├── models.py            # Pydantic data models
│   ├── config.py            # Configuration loader
│   ├── startup.py           # Startup validation logic
│   └── services/
│       ├── __init__.py
│       └── perplexity_client.py  # Perplexity API wrapper
├── config/
│   ├── local_settings.json  # Local config (gitignored)
│   └── local_settings.json.example  # Example template
├── public/                  # Frontend assets (planned)
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── requirements.txt         # Python dependencies
└── README.md               # User-facing documentation
```

## Development Notes

### Error Handling

- Backend services should wrap external API calls with try/except
- Return structured error responses: `{ "error": "message" }`
- Frontend should display user-friendly error messages
- Never expose sensitive information in error messages

### Performance Considerations

- Parallelize topic fetches where possible
- Target response time: <3s for 3 topics
- Request timeout: 10s for external API calls

### Code Quality Standards

- Use explicit Python type hints
- Follow PEP 8 conventions
- CamelCase for classes/types, snake_case for functions/variables
- Add comments only for non-trivial logic
- Keep functions small and readable

