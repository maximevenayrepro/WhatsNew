# WhatsNew

A lightweight local prototype for a "What's New" dashboard. The backend will use FastAPI, and the frontend will be a simple static page. Future tasks plan to integrate Perplexity for fetching recent items per selected topics.

## Python Virtual Environment

Create and activate a local virtual environment before installing any dependencies.

1) Create the environment (all platforms):

```bash
python -m venv .venv
```

2) Activate the environment:

- Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows (CMD):
```cmd
\.venv\Scripts\activate.bat
```

- macOS/Linux (bash/zsh):
```bash
source .venv/bin/activate
```

## Install Requirements

Install dependencies after activating the virtual environment:

```bash
pip install -r requirements.txt
# or
python -m pip install -r requirements.txt
```

To deactivate later, run:

```bash
deactivate
```

## Configuration

Before running the server, create a local configuration file with your Perplexity API key:

1. Copy the example configuration file:
```bash
cp config/local_settings.json.example config/local_settings.json
```

2. Edit `config/local_settings.json` and replace `pplx-YOUR-API-KEY-HERE` with your actual Perplexity API key.

**Important:** The `config/local_settings.json` file is gitignored and should never be committed to version control.


## Run the Server

After installing requirements and activating the virtual environment, start the FastAPI app with Uvicorn:

```powershell
uvicorn server.main:app --reload
```

The server listens on `http://127.0.0.1:8000` by default.

## Data Models

The backend uses Pydantic models for type-safe request and response payloads:

- **`NewsItem`**: Represents a single news article with `title`, `snippet`, `url`, and `topic` fields
- **`TopicRequest`**: Request payload containing a list of topics to query

These models are defined in `server/models.py` and enforce validation rules (e.g., non-empty strings, minimum list length).

## Services

### Perplexity Client

The `PerplexityClient` service (`server/services/perplexity_client.py`) provides a stable interface for searching recent news articles.

**Current implementation**: Returns fake deterministic data to enable frontend development without requiring Perplexity API credentials. The fake data includes sample articles for topics like "technology", "politics", and "sports".

**Usage example**:
```python
from server.services.perplexity_client import PerplexityClient

client = PerplexityClient()
results = client.search_latest(topic="technology", max_results=5)
# Returns a list of NewsItem objects
```

The real Perplexity API integration will replace this fake implementation in a future update.

## Endpoints

- `GET /` — returns plain text `Hello World` (`text/plain`)
- `GET /api/health` — returns JSON `{ "status": "ok" }`

### Quick Test

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/api/health
```
