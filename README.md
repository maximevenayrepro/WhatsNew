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


## Run the Server

After installing requirements and activating the virtual environment, start the FastAPI app with Uvicorn:

```powershell
uvicorn server.main:app --reload
```

The server listens on `http://127.0.0.1:8000` by default.

## Endpoints

- `GET /` — returns plain text `Hello World` (`text/plain`)
- `GET /api/health` — returns JSON `{ "status": "ok" }`

### Quick Test

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/api/health
```
