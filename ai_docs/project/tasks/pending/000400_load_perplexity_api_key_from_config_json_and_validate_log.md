# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Load Perplexity API key from local JSON and validate (log only)

### Goal Statement
**Goal:** Implement reading a local config file (e.g., `config/local_settings.json`) to load `PPLX_API_KEY` and perform a minimal Perplexity API test call; log success/failure without exposing the key.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI, Python stdlib (`json`, `pathlib`), optional `perplexityai`
- **Language:** Python 3.11+
- **Database & ORM:** None
- **UI & Styling:** None in this task
- **Authentication:** API key stored locally (file), never sent to client

### Current State
Server exists with base endpoints. No key loading or validation implemented.

---

## 3. Context & Problem Definition

### Problem Statement
We need a simple, hard-coded way to provide the Perplexity API key for development and ensure connectivity.

### Success Criteria
- [ ] `config/local_settings.json` read at startup
- [ ] Key stored in memory (module-level)
- [ ] Test call executed (search 1 result) and logs success/failure
- [ ] Key never logged or exposed

---

## 4. Development Mode Context
- Local-only; key resides in local file not committed (add `.gitignore` rule)

---

## 5. Technical Requirements

### Functional Requirements
- Read JSON file for `PPLX_API_KEY`
- Perform a lightweight Perplexity API call to validate
- Log result without leaking key

### Non-Functional Requirements
- Fail gracefully if file missing or key invalid
- 10s timeout for the validation request

### Technical Constraints
- If SDK unavailable, use `requests` to call the API

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
- Add `config/` module or helper in `server/` to load settings

---

## 8. Frontend Changes
None.

---

## 9. Implementation Plan
- Create `config/local_settings.json` sample and `.gitignore` rule
- Implement `server/config.py` to load JSON at startup
- Add `server/startup.py` to validate key with a test call (log only)
- Wire startup event in `server/main.py`

---

## 10. Task Completion Tracking
- Logs show success/failure without exposing secrets

---

## 11. File Structure & Organization
- `server/config.py`, `server/startup.py`
- `config/local_settings.json` (local only)

---

## 12. AI Agent Instructions
1) Implement JSON load helper
2) Add startup event and validation call
3) Ensure secrets are not logged

---

## 13. Second-Order Impact Analysis
Enables secure local development; sets foundation for Perplexity integration.


