# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Render static topics as checkboxes and a Refresh button

### Goal Statement
**Goal:** Hardcode a small list of topics (e.g., Tech, Crypto, Space) and render them as checkboxes in the frontend with a Refresh button; no API calls yet.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** None (vanilla JS)
- **Language:** JavaScript (ES6)
- **Database & ORM:** None

### Current State
Frontend skeleton exists with placeholders. No topics UI yet.

---

## 3. Context & Problem Definition

### Problem Statement
User needs to select topics to fetch news for. Start with hardcoded topics.

### Success Criteria
- [ ] Hardcoded topics array in `app.js`
- [ ] Rendered checkboxes and labels in topics section
- [ ] Refresh button present and clickable (no action yet)

---

## 4. Development Mode Context
Local-only; keep it simple and readable.

---

## 5. Technical Requirements

### Functional Requirements
- Add `const topics = ["Tech", "Crypto", "Space"]` to `app.js`
- Render checkboxes on page load
- Add Refresh button with basic click handler stub

### Non-Functional Requirements
- Accessible labels and proper input IDs

### Technical Constraints
- No frameworks

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
None.

---

## 8. Frontend Changes
- Update `public/app.js` and `public/index.html`

---

## 9. Implementation Plan
- Define topics array
- Render checkbox list dynamically
- Add Refresh button and attach a click handler (TODO for next task)

---

## 10. Task Completion Tracking
- Checkboxes appear; Refresh button visible

### Documentation Updates
- Update `README.md` only for user-facing changes (features, installation, run instructions)
- Update `ARCHITECTURE.md` for technical changes (data models, services, API endpoints, architecture)

---

## 11. File Structure & Organization
- `public/app.js`, `public/index.html`

---

## 12. AI Agent Instructions
1) Implement render function for topics
2) Add basic handler for Refresh button

### Testing Procedure
**🚨 CRITICAL:** Before testing any changes, always follow the complete testing sequence defined in `.cursor/local-testing-procedure.mdc`:

1. **Clean port 8000**: Kill any existing process
2. **Setup venv**: Create/activate virtual environment and install dependencies
3. **Launch server**: `venv\Scripts\Activate.ps1; uvicorn server.main:app --reload`
4. **Verify health**: Test `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`

⚠️ **Never skip venv activation before running uvicorn** - it will fail with "command not found"

---

## 13. Second-Order Impact Analysis
Prepares for wiring backend calls in the next task.


