---
description: Maintain concise README and run instructions for local setup and usage
globs: "README.md,ai_docs/**/*.md"
alwaysApply: true
---
# README and Runbook

## Overview
This rule ensures the project has clear, minimal, and accurate run instructions and environment setup documentation for smooth onboarding.

## Rule: Keep docs accurate and minimal
1. **Always** document environment variables and how to set them (`.env.example`).
2. **Always** include setup steps: venv, install deps, run server, open UI.
3. **Never** include secrets in examples; use placeholders.
4. **Always** update docs when endpoints or configs change.

## Common Violations and Solutions

### ❌ BAD: Missing env description
```
Run server
```

### ✅ GOOD: Minimal, actionable steps
```
python -m venv .venv
pip install -r requirements.txt
uvicorn server.main:app --reload
```

## When You Think You Need Exceptions
### Temporary changes
Add a short note in README until code stabilizes.

## Specific Project Patterns
List endpoints: `/api/get_news`, `/api/set_key`, `/api/health`. Mention CORS and localhost.

## Alternative Solutions
Short `Makefile` or PowerShell script for common tasks (optional).

## Tool Configuration (Optional)
```json
{
  "docs": {
    "checkConsistencyOnCI": false
  }
}
```

## Checklist for the Assistant
- [ ] Provide `.env.example` and usage steps
- [ ] Keep endpoints documented and up to date
- [ ] Use placeholders for secrets
- [ ] Update when configs or ports change


