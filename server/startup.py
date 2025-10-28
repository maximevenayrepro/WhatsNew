"""Startup validation for the WhatsNew application.

Performs a minimal Perplexity API test call to validate connectivity and API key.
"""

import logging
from typing import Any, Dict

import requests

from server.config import getConfig


logger = logging.getLogger(__name__)

VALIDATION_TIMEOUT_SECONDS: int = 30
PERPLEXITY_API_URL: str = "https://api.perplexity.ai/chat/completions"


def validatePerplexityApiKey() -> None:
    """Validate the Perplexity API key by making a minimal test request.

    Logs success or failure without exposing the API key.

    Raises:
        RuntimeError: If the API key validation fails.
    """
    config = getConfig()
    apiKey: str = config.perplexityApiKey

    headers: Dict[str, str] = {
        "Authorization": f"Bearer {apiKey}",
        "Content-Type": "application/json",
    }

    # Minimal test payload to validate connectivity
    payload: Dict[str, Any] = {
        "model": "sonar",
        "messages": [
            {
                "role": "user",
                "content": "Hello",
            }
        ],
    }

    try:
        logger.info("Validating Perplexity API key...")
        response = requests.post(
            PERPLEXITY_API_URL,
            headers=headers,
            json=payload,
            timeout=VALIDATION_TIMEOUT_SECONDS,
        )

        if response.status_code == 200:
            logger.info("Perplexity API key validation succeeded")
        elif response.status_code == 401:
            logger.error("Perplexity API key validation failed: Unauthorized (401)")
            raise RuntimeError(
                "Invalid Perplexity API key. Please check config/local_settings.json"
            )
        else:
            errorDetail: str = ""
            try:
                errorDetail = response.text[:200]
            except Exception:
                pass
            logger.error(
                "Perplexity API key validation failed with status %d. Response: %s",
                response.status_code,
                errorDetail,
            )
            raise RuntimeError(
                f"Perplexity API validation failed with status {response.status_code}"
            )

    except requests.Timeout as error:
        logger.error("Perplexity API validation timed out after %ds", VALIDATION_TIMEOUT_SECONDS)
        raise RuntimeError(
            f"Perplexity API validation timed out after {VALIDATION_TIMEOUT_SECONDS}s"
        ) from error

    except requests.RequestException as error:
        logger.error("Perplexity API validation request failed: %s", type(error).__name__)
        raise RuntimeError("Perplexity API validation request failed") from error

