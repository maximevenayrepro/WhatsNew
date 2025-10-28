# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Create Perplexity service wrapper interface with a fake response

### Goal Statement
**Goal:** Provide a `services/perplexity_client.py` with a clear interface and a temporary fake implementation returning deterministic sample results for development.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI
- **Language:** Python 3.11+
- **Database & ORM:** None
- **Key Architectural Patterns:** Service layer encapsulating external API

### Current State
No Perplexity client exists yet. Key loading/validation is handled separately.

---

## 3. Context & Problem Definition

### Problem Statement
Routes require a stable interface before real API calls are implemented. A fake response helps unblock UI development.

### Success Criteria
- [ ] `server/services/perplexity_client.py` created
- [ ] `search_latest(topic: str, max_results: int) -> list[NewsItem]` defined
- [ ] Returns 1-3 deterministic fake `NewsItem` entries per call

---

## 4. Development Mode Context
Local prototype; allow fake data for early integration.

---

## 5. Technical Requirements

### Functional Requirements
- Implement a class `PerplexityClient` with `search_latest`
- Accept `topic` and `max_results`
- Return fake `NewsItem` list using the models module

### Non-Functional Requirements
- Keep implementation small and side-effect free

### Technical Constraints
- Do not call external network here (real call added in a later task)

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
No new routes; service only.

---

## 8. Frontend Changes
None.

---

## 9. Implementation Plan
- Create `server/services/perplexity_client.py`
- Implement `PerplexityClient.search_latest`
- Use `NewsItem` from `server/models.py`

---

## 10. Task Completion Tracking
- Service can be imported and called from a REPL
- README updated to reflect this task (summary and usage impact)

---

## 11. File Structure & Organization
- `server/services/perplexity_client.py`

---

## 12. AI Agent Instructions
1) Create the wrapper with a fake implementation
2) Add docstrings and explicit types

---

## 13. Second-Order Impact Analysis
Allows backend and frontend integration before real API dependency.


