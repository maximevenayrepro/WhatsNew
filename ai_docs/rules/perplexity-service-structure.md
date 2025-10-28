---
description: Structure and practices for the Perplexity service wrapper and related files
globs: "server/**/*.py,**/*.py"
alwaysApply: true
---
# Perplexity Service and Project Structure

## Overview
This rule standardizes how we integrate with the Perplexity API, organize files, and isolate external calls behind a clean interface.

## Rule: Isolate external API logic in a service layer
1. **Always** wrap Perplexity calls in `services/perplexity_client.py` with small, typed functions.
2. **Always** keep request building and response parsing in separate helpers.
3. **Never** call the Perplexity API directly from route handlers.
4. **Always** map upstream errors to internal exceptions (e.g., `ExternalServiceTimeoutError`).
5. **Always** cap results to 5 and filter required fields `{ title, snippet, url, topic }`.

## Common Violations and Solutions

### ❌ BAD: Inline HTTP calls inside routes
```python
@router.post("/api/get_news")
def get_news(...):
    # direct HTTP call here
    ...
```

### ✅ GOOD: Delegation to service layer
```python
items = perplexityService.search_topics(topics=topics, window_hours=24, max_results=5)
```

## When You Think You Need Exceptions
### Quick diagnostics
Use a dedicated `/api/health` that does not contact Perplexity, only local checks.

## Specific Project Patterns
```python
# ✅ GOOD: File structure
# server/main.py
# server/models.py
# server/services/perplexity_client.py
# server/routes/news.py
# server/routes/settings.py
```

## Alternative Solutions
### 1. Use `requests` with a tiny wrapper if SDK is unavailable
### 2. Provide a mock service for offline development/testing

## Tool Configuration (Optional)
```json
{
  "perplexity": {
    "maxResults": 5,
    "windowHours": 24
  }
}
```

## Checklist for the Assistant
- [ ] Keep all Perplexity calls inside the service layer
- [ ] Separate request build, call, and parse steps
- [ ] Map upstream errors to internal exceptions
- [ ] Enforce limits and field filtering


