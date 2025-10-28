# AI Task Planning Template - Starter Framework

> **About This Template:** This is a systematic framework for planning and executing technical projects with AI assistance. Use this structure to break down complex features, improvements, or fixes into manageable, trackable tasks that AI agents can execute effectively.

---

## 1. Task Overview

### Task Title
<!-- Give your task a clear, specific name that describes what you're building or fixing -->
**Title:** [Brief, descriptive title - e.g., "Add User Authentication System" or "Fix Payment Integration Bug"]

### Goal Statement
<!-- Write one paragraph explaining what you want to achieve and why it matters for your project -->
**Goal:** [Clear statement of the end result you want and the business/user value it provides]

---

## 2. Project Analysis & Current State

### Technology & Architecture
<!-- This is where you document your current tech stack so the AI understands your environment -->
- **Frameworks & Versions:** TODO: List your main frameworks and versions
- **Language:** Python 3.11+; JavaScript (ES6)
- **Database & ORM:** None for MVP; optional local JSON config (no ORM)
- **UI & Styling:** Static HTML/CSS with minimal custom CSS; no framework
- **Authentication:** None (local-only). Perplexity API key stored server-side (env or in-memory)
- **Key Architectural Patterns:** REST API, service layer for Perplexity, simple MVC separation, env-based config

### Current State
<!-- Describe what exists today - what's working, what's broken, what's missing -->
[Analysis of your current codebase state, existing functionality, and what needs to be changed]

## 3. Context & Problem Definition

### Problem Statement
<!-- This is where you clearly define the specific problem you're solving -->
[Detailed explanation of the problem, including user impact, pain points, and why it needs to be solved now]

### Success Criteria
<!-- Define exactly how you'll know when this task is complete and successful -->
- [ ] [Specific, measurable outcome 1]
- [ ] [Specific, measurable outcome 2]
- [ ] [Specific, measurable outcome 3]

---

## 4. Development Mode Context

### Development Mode Context
<!-- This is where you tell the AI agent about your project's constraints and priorities -->
- **🚨 Project Stage:** New development (local prototype)
- **Breaking Changes:** Acceptable during MVP; stabilize API endpoints once UI integrates
- **Data Handling:** No user data; store API key securely (never exposed to client). Optional local config file
- **User Base:** Single local user (solo prototype)
- **Priority:** Speed to MVP, then stability; minimize external dependencies

---

## 5. Technical Requirements

### Functional Requirements
<!-- This is where the AI will understand exactly what the system should do - be specific about user actions and system behaviors -->

- User can select topics to include via checkboxes
- User can click "Refresh News" to fetch latest results
- User can click a result to open a modal with details and a link
- User can input/validate the Perplexity API key via an Options panel
- System fetches up to 5 results per selected topic for the last 24 hours
- System renders one-line summaries (title or first sentence of snippet)
- System handles errors/timeouts gracefully and shows empty/error states
- System never exposes the API key to the client (server-side only)
- System supports instant hide/show of topic sections in the UI

### Non-Functional Requirements
<!-- This is where you define performance, security, and usability standards -->
- **Performance:** Parallelize topic fetches; target <3s for 3 topics; 10s request timeout
- **Security:** API key stored server-side; validate on set; do not log secrets; restrict CORS to localhost
- **Usability:** One-line summaries; clear topic sections; accessible modal (Esc to close, focus trap)
- **Responsive Design:** Desktop-first; basic responsiveness down to 320px width for MVP
- **Theme Support:** Light theme for MVP; optional dark mode in roadmap

### Technical Constraints
<!-- This is where you list limitations the AI agent must work within -->
- [Must use existing system X]
- [Cannot modify database table Y]
- [Must maintain compatibility with feature Z]

---

## 6. Data & Database Changes

### Database Schema Changes
<!-- This is where you specify any database modifications needed -->

No database for MVP; no SQL schema changes

### Data Model Updates
<!-- This is where you define TypeScript types, schema updates, or data structure changes -->

Python models (dataclasses or pydantic):
- NewsItem: { title: str, snippet: str, url: str, topic: str }
- TopicRequest: { topics: list[str] }

Frontend JS data shapes:
- NewsItem: { title: string, snippet: string, url: string, topic: string }
- Settings (client-side): { selectedTopics: string[] }

### Data Migration Plan
<!-- This is where you plan how to handle existing data during changes -->

Not applicable (no persistent DB). If later persisting settings, version the JSON and provide a simple upgrade path

---

## 7. API & Backend Changes

### Data Access Pattern Rules
<!-- This is where you tell the AI agent how to structure backend code in your project -->

Routes in server (e.g., `routes/news.py`, `routes/settings.py`); Perplexity integration in `services/perplexity_client.py`; response models in `models.py`; config via env or `config.py`

### Server Actions
<!-- List the backend mutation operations you need -->

- POST `/api/set_key`: store/validate Perplexity API key in memory or local secure store
- POST `/api/get_news`: accept topics array, return news by topic (max 5 each)
- GET `/api/health`: health check

### Database Queries
<!-- Specify how you'll fetch data -->

No database. Data fetched via Perplexity service; encapsulate external API calls in `services/perplexity_client.py`

---

## 8. Frontend Changes

### New Components
<!-- This is where you specify UI components to be created -->

- TopicSelector: manage topic checkboxes
- NewsSection: render topic header and list of news items
- NewsItemRow: single-line summary with link/details trigger
- Modal: display article title/snippet/link
- OptionsPanel: input and submit API key

### Page Updates
<!-- This is where you list pages that need modifications -->

- Create `index.html` with sections: options, topic selection, results container, modal root
- Wire up buttons and placeholders for dynamic rendering

### State Management
<!-- This is where you plan how data flows through your frontend -->

- In-memory JS state: { selectedTopics, newsByTopic, isLoading }
- Persist `selectedTopics` in `localStorage`
- Fetch news on demand; re-render sections per topic

---

## 9. Implementation Plan

Phase 1 – Project setup:
- `server/main.py` FastAPI app skeleton; env loading; CORS for localhost

Phase 2 – Perplexity service:
- `server/services/perplexity_client.py` wrapper (search last 24h, max 5)
- `server/models.py` response/request models

Phase 3 – API routes:
- `server/routes/news.py` `/api/get_news`
- `server/routes/settings.py` `/api/set_key`, `/api/health`

Phase 4 – Frontend skeleton:
- `public/index.html`, `public/styles.css`, `public/app.js`

Phase 5 – UI interactions:
- Topic selection, refresh button, modal behavior, error/empty states

Phase 6 – Validation & polish:
- Key validation flow, parallel fetch, minimal styling

---

## 10. Task Completion Tracking

### Real-Time Progress Tracking
<!-- This is where you tell the AI agent to update progress as work is completed -->

Track via concise status updates per milestone; log server events; AI agent updates TODO statuses upon completing phases

### Documentation Updates
- Update `README.md` only for user-facing changes (features, installation, run instructions)
- Update `ARCHITECTURE.md` for technical changes (data models, services, API endpoints, architecture)

---

## 11. File Structure & Organization

Planned structure:
- `server/main.py`, `server/models.py`, `server/services/perplexity_client.py`
- `server/routes/news.py`, `server/routes/settings.py`
- `public/index.html`, `public/styles.css`, `public/app.js`
- `README.md`, `.env.example`

---

## 12. AI Agent Instructions

### Implementation Workflow
<!-- This is where you give specific instructions to your AI agent -->
🎯 **MANDATORY PROCESS:**
1) Create venv and install deps (FastAPI, uvicorn, perplexityai or requests)
2) Implement models and Perplexity service wrapper
3) Add API routes (`/api/get_news`, `/api/set_key`, `/api/health`) with validation
4) Build frontend (`index.html`, `app.js`, `styles.css`) and wire interactions
5) Test end-to-end locally; handle errors, empty states, timeouts
6) Secure key handling (server-only), restrict CORS, avoid logging secrets
7) Document run instructions and environment variables

### Testing Procedure
<!-- Always follow the local testing procedure rule -->
**🚨 CRITICAL:** Before testing any changes, always follow the complete testing sequence defined in `.cursor/local-testing-procedure.mdc`:

1. **Clean port 8000**: Kill any existing process
2. **Setup venv**: Create/activate virtual environment and install dependencies
3. **Launch server**: `venv\Scripts\Activate.ps1; uvicorn server.main:app --reload`
4. **Verify health**: Test `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`

⚠️ **Never skip venv activation before running uvicorn** - it will fail with "command not found"

See `.cursor/local-testing-procedure.mdc` for complete PowerShell commands and troubleshooting.

### Communication Preferences
<!-- This is where you set expectations for how the AI should communicate -->
Concise French status updates; code and comments in English; highlight blockers/risks early; summarize impacts after each phase

### Code Quality Standards
<!-- This is where you define your coding standards for the AI to follow -->
Explicit typing (Python type hints); small, readable functions; PEP 8; meaningful names; handle exceptions with clear messages; comments only for non-trivial logic; no secrets in client code

---

## 13. Second-Order Impact Analysis

### Impact Assessment
<!-- This is where you think through broader consequences of your changes -->

Risks/impacts:
- External API cost/rate limits; parallel requests may throttle
- Key exposure risk if mishandled; ensure server-only storage and sanitized logs
- Network timeouts impacting UX; add loading states and retries/backoff
- CORS/security misconfig could block frontend calls; restrict to localhost
- Modal accessibility and responsive layout to avoid blocking user flow

