# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Basic error handling and empty states (backend and frontend)

### Goal Statement
**Goal:** Implement minimal error handling on the backend and show user-friendly empty/error states on the frontend.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI, vanilla JS
- **Language:** Python 3.11+, JavaScript (ES6)

### Current State
End-to-end flow works but lacks robust error/empty handling.

---

## 3. Context & Problem Definition

### Problem Statement
Network/API failures and no-results cases should be handled gracefully.

### Success Criteria
- [ ] Backend returns structured error responses with clear messages
- [ ] Frontend displays empty-state for no items
- [ ] Frontend displays an error banner/message on failure

---

## 4. Development Mode Context
Local-only; concise, non-verbose messages.

---

## 5. Technical Requirements

### Functional Requirements
- Wrap service calls with try/except; return 4xx/5xx appropriately
- Add client-side error boundary for fetch failures
- Display simple empty-state per topic (e.g., "No results")

### Non-Functional Requirements
- Do not leak sensitive information in error messages

### Technical Constraints
- Keep implementation small and maintainable

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
- Consistent error response shape `{ error: string }`

---

## 8. Frontend Changes
- Update `public/app.js` to handle empty and error states

---

## 9. Implementation Plan
- Add error handling helpers in backend
- Update route to use helpers
- Update frontend fetch/render to show messages

---

## 10. Task Completion Tracking
- Simulate failures and verify UI messages

### Documentation Updates
- Update `README.md` only for user-facing changes (features, installation, run instructions)
- Update `ARCHITECTURE.md` for technical changes (data models, services, API endpoints, architecture)

---

## 11. File Structure & Organization
- `server/` routes and possibly `server/utils/errors.py`
- `public/app.js`

---

## 12. AI Agent Instructions
1) Implement minimal error helpers
2) Update route and frontend to use them

### Testing Procedure
**🚨 CRITICAL:** Before testing any changes, always follow the complete testing sequence defined in `.cursor/local-testing-procedure.mdc`:

1. **Clean port 8000**: Kill any existing process
2. **Setup venv**: Create/activate virtual environment and install dependencies
3. **Launch server**: `venv\Scripts\Activate.ps1; uvicorn server.main:app --reload`
4. **Verify health**: Test `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`

⚠️ **Never skip venv activation before running uvicorn** - it will fail with "command not found"

---

## 13. Second-Order Impact Analysis
Improves reliability and user trust in the MVP.


