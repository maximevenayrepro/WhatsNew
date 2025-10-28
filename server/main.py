"""FastAPI application exposing a root Hello World and a health check endpoint.

This minimal server validates the stack and provides a base for future routes.
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app: FastAPI = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def read_root() -> str:
    """Return a plain text greeting to confirm the server is running."""
    return "Hello World"


@app.get("/api/health")
def get_health() -> Dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


