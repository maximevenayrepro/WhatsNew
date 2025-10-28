---
description: Enforce concise, useful comments and docstrings only for non-trivial logic
globs: "server/**/*.py,**/*.py,public/**/*.js,public/**/*.html"
alwaysApply: true
---
# Comments and Docstrings

## Overview
This rule ensures comments and docstrings are purposeful, concise, and written only when they add real value. Comments should explain the why, not restate the what.

## Rule: Comment intent, not obvious code
1. **Never** add comments that restate straightforward code.
2. **Always** add docstrings to Python public APIs, routes, and services.
3. **Always** document non-trivial invariants, edge cases, and security constraints.
4. **Never** leave TODO comments—implement the change or create a tracked task.
5. **Always** write comments and docstrings in English.

## Common Violations and Solutions

### ❌ BAD: Obvious comments
```python
# increment i
i = i + 1
```

### ✅ GOOD: Explain non-obvious rationale
```python
def fetchNewsWithTimeout(...):
    """Fetch news with a strict timeout to keep UI responsive and avoid hanging requests."""
    ...
```

### ❌ BAD: JS comment restating the code
```javascript
// set value
state.value = v;
```

### ✅ GOOD: Note an important constraint
```javascript
// Avoid logging sensitive data returned by the server
state.lastUpdatedAt = Date.now();
```

## When You Think You Need Exceptions
### Trivial private helpers
```python
# ✅ GOOD: No docstring needed if name is self-explanatory and scope is local
def isEmpty(text: str) -> bool:
    return text.strip() == ""
```

## Specific Project Patterns
```python
def get_news(...):
    """Route handler for fetching news. Returns 5 items per topic for the last 24h."""
    ...
```

```javascript
/**
 * Initialize modal with accessibility behavior (focus trap, Esc to close).
 */
function initModal() { /* ... */ }
```

## Alternative Solutions
### 1. Use type names and function names to remove the need for comments
```python
def parsePerplexitySearchResponse(...):
    ...
```

### 2. Keep high-level docs in README for flows instead of inline walls of comments

## Tool Configuration (Optional)
```json
{
  "lint": {
    "maxLineLength": 100
  }
}
```

## Checklist for the Assistant
- [ ] Add docstrings to public Python APIs and services
- [ ] Comment only non-trivial logic, constraints, and invariants
- [ ] Remove/avoid TODO comments; create tasks instead
- [ ] Keep comments concise and in English


