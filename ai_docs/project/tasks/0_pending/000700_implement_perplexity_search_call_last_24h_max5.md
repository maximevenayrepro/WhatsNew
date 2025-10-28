# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Implement Perplexity search call (last 24h, max 5 results)

### Goal Statement
**Goal:** Replace the fake implementation with a real Perplexity API call in the service wrapper to fetch up to 5 results for the last 24 hours for a given topic.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI, `perplexityai` SDK or `requests`
- **Language:** Python 3.11+
- **Database & ORM:** None
- **Key Architectural Patterns:** Service layer for external API

### Current State
Service wrapper exists with a fake implementation and key loading/validation.

---

## 3. Context & Problem Definition

### Problem Statement
We need real data from Perplexity to power the MVP.

### Success Criteria
- [ ] `PerplexityClient.search_latest` performs real API call
- [ ] Query format: "latest news about <topic> in the past 24 hours"
- [ ] Returns up to 5 mapped `NewsItem` objects
- [ ] 10s timeout and graceful error handling

---

## 4. Development Mode Context
Local; log minimal errors (without secrets). Handle timeouts.

---

## 5. Technical Requirements

### Functional Requirements
- Implement real call using SDK or `requests`
- Map response fields to `NewsItem`
- Limit results to `max_results`

### Non-Functional Requirements
- Avoid logging secrets; concise error messages
- Basic retry optional (single retry)

### Technical Constraints
- Use key from `server/config.py`

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
- Update `server/services/perplexity_client.py` replacing fake implementation
- Add timeout and minimal exception handling
- Manually test via Python REPL

---

## 10. Task Completion Tracking
- Verified real results for sample topics (e.g., "Tech")

---

## 11. File Structure & Organization
- `server/services/perplexity_client.py`

---

## 12. AI Agent Instructions
1) Implement real request
2) Map fields and return typed results
3) Handle errors gracefully

---

## 13. Second-Order Impact Analysis
Enables end-to-end data flow using real news.


