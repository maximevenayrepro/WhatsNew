# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Call backend `/api/get_news` on Refresh and render items by topic

### Goal Statement
**Goal:** On Refresh click, collect selected topics, call the backend `POST /api/get_news`, and render one-line results grouped by topic.

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** None (vanilla JS)
- **Language:** JavaScript (ES6)
- **Database & ORM:** None

### Current State
Frontend shows topics and a Refresh button. Backend route exists.

---

## 3. Context & Problem Definition

### Problem Statement
We need to connect UI interactions to the backend and display results.

### Success Criteria
- [ ] On click, selected topics are sent to `/api/get_news`
- [ ] Results render as `<ul>` lists under each topic section
- [ ] Each item shows a single-line summary (title or snippet first sentence)

---

## 4. Development Mode Context
Local-only; simple rendering with minimal styling.

---

## 5. Technical Requirements

### Functional Requirements
- Build request payload: `{ topics: string[] }`
- Use `fetch` with JSON body
- Render grouped results by topic

### Non-Functional Requirements
- 10s client-side fetch timeout (AbortController)
- Basic empty-state messages

### Technical Constraints
- Respect CORS restrictions

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
None.

---

## 8. Frontend Changes
- Update `public/app.js` to wire the flow and render results

---

## 9. Implementation Plan
- Implement function to collect selected topics
- Implement `fetchNews(topics)` with timeout
- Render results into DOM grouped by topic

---

## 10. Task Completion Tracking
- Manual test: select topics, click Refresh, see results/empty-state
- README updated to reflect this task (summary and usage impact)

---

## 11. File Structure & Organization
- `public/app.js`

---

## 12. AI Agent Instructions
1) Wire event handlers
2) Implement fetch and render functions

---

## 13. Second-Order Impact Analysis
Provides end-to-end MVP behavior.


