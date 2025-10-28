---
description: Protect secrets, use env config, and restrict CORS to localhost
globs: "server/**/*.py,**/*.py,public/**/*.js"
alwaysApply: true
---
# Secrets, Configuration, and CORS

## Overview
This rule ensures the Perplexity API key and configuration are handled securely on the server, never exposed to the client, with CORS restricted to localhost during development.

## Rule: Do not expose secrets
1. **Never** expose `PPLX_API_KEY` to the client or embed it in JS/HTML.
2. **Always** load secrets from environment variables or a secure local store.
3. **Never** log secrets or sensitive headers; sanitize logs.
4. **Always** restrict CORS to trusted origins (localhost only for MVP).
5. **Always** provide a `.env.example` and document required variables.

## Common Violations and Solutions

### ❌ BAD: API key in frontend code
```javascript
// Do not do this
const PPLX_API_KEY = "sk-...";
```

### ✅ GOOD: Server-only key access
```python
import os

PPLX_API_KEY: str | None = os.getenv("PPLX_API_KEY")
if not PPLX_API_KEY:
    raise RuntimeError("PPLX_API_KEY is required")
```

### ❌ BAD: Permissive CORS
```python
allow_origins=["*"]
```

### ✅ GOOD: Restrictive CORS for local development
```python
allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"]
```

## When You Think You Need Exceptions
### Testing in a different local port
Add that port explicitly to allowed origins, do not use wildcard `*`.

## Specific Project Patterns
```python
# ✅ GOOD: Centralize env loading
class AppConfig(BaseModel):
    perplexityApiKey: str
    allowedOrigins: list[str]
```

## Alternative Solutions
### 1. Use in-memory storage for submitted key via `/api/set_key`
### 2. Use a local file with restricted permissions if needed (avoid committing it)

## Tool Configuration (Optional)
```json
{
  "env": {
    "required": ["PPLX_API_KEY"]
  }
}
```

## Checklist for the Assistant
- [ ] Never put secrets in client code or logs
- [ ] Load keys from env or server-only store
- [ ] Restrict CORS to localhost origins only
- [ ] Provide `.env.example` and docs


