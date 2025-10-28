"""FastAPI application exposing a root Hello World and a health check endpoint.

This minimal server validates the stack and provides a base for future routes.
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse


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


@app.get("/", response_class=PlainTextResponse)
def read_root() -> str:
    """Return a plain text greeting to confirm the server is running."""
    return "Hello World"


@app.get("/api/health")
def get_health() -> Dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


