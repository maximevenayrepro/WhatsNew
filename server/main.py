"""FastAPI application exposing a root Hello World and a health check endpoint.

This minimal server validates the stack and provides a base for future routes.
"""

import logging
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from server.config import loadConfig
from server.startup import validatePerplexityApiKey


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


@app.get("/", response_class=PlainTextResponse)
def read_root() -> str:
    """Return a plain text greeting to confirm the server is running."""
    return "Hello World"


@app.get("/api/health")
def get_health() -> Dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


