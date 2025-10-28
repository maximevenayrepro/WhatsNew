# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Add POST `/api/get_news` route and wire Perplexity service

### Goal Statement
**Goal:** Implement a backend route that accepts a list of topics and returns aggregated `NewsItem` results per topic using the service layer.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI, Pydantic
- **Language:** Python 3.11+
- **Database & ORM:** None
- **Key Architectural Patterns:** Routes delegate to service layer

### Current State
Models and service wrapper exist. No `get_news` route yet.

---

## 3. Context & Problem Definition

### Problem Statement
Frontend requires a single endpoint to fetch news results for selected topics.

### Success Criteria
- [ ] `POST /api/get_news` accepts `TopicRequest`
- [ ] Returns `{ topic: string, items: NewsItem[] }[]`
- [ ] Uses service to fetch up to 5 per topic
- [ ] Handles errors and empty results gracefully

---

## 4. Development Mode Context
Local; topics hardcoded client-side initially.

---

## 5. Technical Requirements

### Functional Requirements
- Validate request payload
- For each topic, call service `search_latest(topic, max_results=5)`
- Aggregate results into response structure

### Non-Functional Requirements
- 10s request timeout overall (simple guard)
- Minimal logging, no secrets

### Technical Constraints
- Use existing models and service

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
- Add route in `server/routes/news.py` (or inside `main.py` if simpler for MVP)

---

## 8. Frontend Changes
None in this task.

---

## 9. Implementation Plan
- Create `server/routes/news.py` with router and route handler
- Register router in `server/main.py`
- Implement aggregation logic and return typed response

---

## 10. Task Completion Tracking
- cURL or HTTPie test returns expected JSON structure

### Documentation Updates
- Update `README.md` only for user-facing changes (features, installation, run instructions)
- Update `ARCHITECTURE.md` for technical changes (data models, services, API endpoints, architecture)

---

## 11. File Structure & Organization
- `server/routes/news.py`

---

## 12. AI Agent Instructions
1) Implement POST route
2) Wire service and models
3) Test with sample topics

### Testing Procedure
**🚨 CRITICAL:** Before testing any changes, always follow the complete testing sequence defined in `.cursor/local-testing-procedure.mdc`:

1. **Clean port 8000**: Kill any existing process
2. **Setup venv**: Create/activate virtual environment and install dependencies
3. **Launch server**: `venv\Scripts\Activate.ps1; uvicorn server.main:app --reload`
4. **Verify health**: Test `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`

⚠️ **Never skip venv activation before running uvicorn** - it will fail with "command not found"

**Note:** For this documentation task, include these testing instructions in the README.md run instructions.


---

## 13. Second-Order Impact Analysis
Unblocks frontend integration for fetching news.


