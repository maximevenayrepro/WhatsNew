"""FastAPI application serving the frontend and exposing API endpoints.

This server provides the What's New dashboard frontend and REST API for news search.
"""

import logging
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from server.config import loadConfig
from server.startup import validatePerplexityApiKey
from server.routes.news import router as news_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


app: FastAPI = FastAPI()

# Configure strict CORS for local development only
allowed_origins: list[str] = [
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=False,
)

# Register API routers
app.include_router(news_router)


@app.on_event("startup")
def onStartup() -> None:
    """Load configuration and validate Perplexity API key on application startup."""
    logger.info("Starting WhatsNew application...")
    try:
        loadConfig()
        validatePerplexityApiKey()
        logger.info("Application startup complete")
    except Exception as error:
        logger.error("Startup failed: %s", error)
        raise


@app.get("/api/health")
def get_health() -> Dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


# Mount static files for CSS and JS
app.mount("/", StaticFiles(directory="public", html=True), name="static")


