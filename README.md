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

## Access the Application

Once the server is running, open your browser and navigate to:

```
http://127.0.0.1:8000
```

This will load the frontend dashboard. The page includes:
- Topic selection area (coming soon)
- News results display (coming soon)
- Modern, responsive UI

## Features

### Current Features

- FastAPI backend with health check endpoint
- Configuration management for Perplexity API key
- News search service integrated with Perplexity AI
- Frontend skeleton with modern UI
- Static file serving

### Planned Features

- Dynamic topic selection with checkboxes
- Real-time news fetching via "Refresh News" button
- Modal view for article details
- Error handling and empty states
- Loading indicators

## Quick Test

Test the running server:

```bash
# Test health endpoint
curl http://127.0.0.1:8000/api/health

# Test news API with topics
curl -X POST http://127.0.0.1:8000/api/get_news \
  -H "Content-Type: application/json" \
  -d '{"topics": ["technology", "Python"]}'
```

## Documentation

For technical details about the architecture, data models, services, and API endpoints, see [ARCHITECTURE.md](ARCHITECTURE.md).
