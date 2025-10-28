## Development Plan for a Daily News Aggregator

### Project Context and Objectives

Each morning, the goal is to provide the user with an ultra-concise summary of news across selected topics (e.g., Tech, Crypto, Space, etc.). The application will be a local website (not external SaaS) accessible from the user's PC. No Google login is required, and only the local user will have access (solo prototype). News data will be fetched in real-time via the Perplexity API using the user-provided API key.

**Key functionalities:**

- **Customizable topic selection**: The user can define a list of topics (e.g., Tech, Crypto, Space) and check/uncheck those they wish to see in the daily summary.
- **Daily concise summary**: For each selected topic, display up to 5 results, each in the form of a single sentence summarizing the main news item.
- **Detail on demand**: When clicking on a result, show the full content or a detailed summary in a popup (without leaving the page).
- **Perplexity API integration**: Use the Perplexity API to search the latest news for each topic and optionally summarize article content. The application must allow the user to enter the Perplexity API key (e.g., in settings or a config file) to perform the necessary calls.

The project should provide a **custom collection of news** based on the user's interests, with an AI-generated concise summary for each article. All of it runs locally every morning using a small Python server that generates a locally viewable webpage.

### Technical Choices (Stack)

**Back-end**: Python with a micro web framework (Flask or FastAPI) to host the app locally. Python is chosen for its script simplicity and availability of the Perplexity SDK. The backend server will serve HTML pages and expose API endpoints to fetch news (and optionally article details).

**Front-end**: Lightweight HTML/CSS/JavaScript web page (possibly with a minimal JS framework, or just vanilla JS/jQuery). The user interface will include:
- A list of checkboxes to select topics to display.
- A button/control to **refresh** news (unless we opt for automatic loading on page load).
- A results section displaying titles or news summaries for each selected topic (each as a clickable sentence).
- A popup window (modal) to show full article details when a result is clicked.

**Perplexity API**: Use the Perplexity Search API to search for news. The typical query will use the *Sonar* model optimized for news (if available), searching for the last 24 hours for each topic. For instance, for the "Tech" topic, the query might be: *"latest news about Tech in the past 24 hours"* with `max_results: 5`. The API will return a list of results with title, URL, and snippet. These can be used to generate summaries.

- *Note about the API key*: The user must provide their Perplexity API key (via a settings field or config file). Without this key, API calls cannot be made. It should be stored securely (e.g., in server memory or a local non-exposed file), and the user must be informed they are responsible for API usage costs.

**Display and UX**: Focused on **readability** and fast browsing. A clean layout will be designed, with sections by topic. The user can check/uncheck topics to filter without fully reloading the page (via client-side JS to show/hide sections or AJAX calls to fetch topics on demand). Each result is shown on a single line, like a concise news headline. Clicking opens a modal with more info.

### Development Steps

1. **Project Initialization**
   - Create a new Python project and set up a virtual environment. Install necessary dependencies: web framework (Flask or FastAPI) and Perplexity SDK (`pip install perplexityai`) or `requests` if calling the API directly.
   - Optionally initialize a Git repository for version tracking.

2. **Perplexity API Setup**
   - API Key: Implement a mechanism to supply the Perplexity API key to the application. Initially use an environment variable or config file (e.g., `PPLX_API_KEY`). Later, add a web UI for input under "Options."
   - Validate the API key by performing a test call:
     ```python
     from perplexity import Perplexity
     client = Perplexity(api_key=MY_API_KEY)
     resp = client.search.create(query="test query", max_results=1)
     print(resp.results[0].title, resp.results[0].url)
     ```

3. **Defining Topics**
   - Start with a static list of topics (e.g., ["Tech", "Crypto", "Space"]). Define them in code or config.
   - Optionally make the list editable via a JSON config or simple UI later.
   - Each topic can directly map to the search query term.

4. **Backend – News Search Route**
   - Implement an API route (e.g., `/api/get_news`) accepting an optional list of topics.
   - For each topic, send a query like `"latest news about <topic> in the past 24 hours"` with `max_results=5`.
   - Optionally use `include_domains` to restrict to trusted sources.
   - Extract and return `{ title, snippet, url }` for each result. Handle errors (timeouts, API errors, empty results).

5. **Frontend – User Interface**
   - Build `index.html` served by Flask/FastAPI or statically. Include:
     - Checkboxes for each topic
     - A "Refresh News" button
     - A container to display results
   - Use JavaScript to:
     - Fetch selected topics
     - Call `/api/get_news` via `fetch`
     - Render results per topic dynamically
   - For each topic, generate:
     - Section header
     - `<ul>` with `<li>` for each result (1-line summary, link or [+] button)
     - Optional icon link to full article

   - **Summary format**:
     - Use article title by default.
     - Optionally use first sentence of `snippet` or summarize using Perplexity completion API.

   - **Instant filtering**:
     - Hide/show sections dynamically with JS
     - MVP: reload on button click is acceptable

   - Add minimal CSS for clarity.

6. **Popup for Result Detail**
   - Implement a modal that shows:
     - Title, `snippet`, and link to full article
   - Optionally use a second API call or scraper to expand article content
   - Keep it simple for MVP: use `snippet` only
   - Add close button and style the modal (centered, dimmed background)

7. **API Key Settings Option**
   - Add a UI section (e.g., gear icon or "Options") to input the API key
   - Backend route `/api/set_key` stores key in memory or config file
   - Key must never be exposed in frontend JS
   - Validate key on input if needed

8. **Testing and Adjustments**
   - Test the full workflow:
     - Open page
     - Click "Refresh News"
     - Validate that 1-line summaries show
     - Test popup behavior
     - Simulate empty or error cases
   - Try various topics
   - Measure response time and optimize (e.g., parallel API calls)

9. **Future Improvements (Roadmap)**
   - **Daily Automation**: Schedule daily data fetch via cron or Python scheduler (e.g., APScheduler)
   - **Improved Summarization**: Use Perplexity’s summarization endpoint or custom prompt
   - **Interactive UX**: Add loading spinners or animations
   - **Source Filtering**: Allow user-defined sources or exclusions
   - **Result/Time Range Settings**: Let user configure max results and timeframe (e.g., 24h, 1w)
   - **Logging**: Store daily logs (JSON) locally for audit or history

### References

- Perplexity API Documentation – *Search API Guide*
- Perplexity Cookbook – *Daily News Briefing (Obsidian)*
- Perplexity Cookbook – *Financial News Tracker*
- Reddit Discussion on Perplexity vs Other APIs

