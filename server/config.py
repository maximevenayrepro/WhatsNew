"""Configuration loader for the WhatsNew application.

Reads local_settings.json and exposes application settings in memory.
"""

import json
import logging
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


logger = logging.getLogger(__name__)


class AppConfig(BaseModel):
    """Application configuration schema."""

    perplexityApiKey: str = Field(..., min_length=1)


_config: Optional[AppConfig] = None


def loadConfig() -> AppConfig:
    """Load and validate configuration from config/local_settings.json.

    Returns:
        AppConfig: Validated configuration object.

    Raises:
        FileNotFoundError: If config file does not exist.
        ValueError: If config is invalid or missing required fields.
    """
    global _config

    if _config is not None:
        return _config

    configPath: Path = Path("config/local_settings.json")

    if not configPath.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {configPath}. "
            "Please copy config/local_settings.json.example and fill in your API key."
        )

    try:
        with open(configPath, "r", encoding="utf-8") as file:
            rawConfig: dict = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {configPath}: {error}") from error

    try:
        _config = AppConfig(**rawConfig)
    except ValidationError as error:
        logger.error("Configuration validation failed: missing or invalid fields")
        raise ValueError(
            f"Configuration validation failed. Ensure 'perplexityApiKey' is present and valid."
        ) from error

    logger.info("Configuration loaded successfully from %s", configPath)
    return _config


def getConfig() -> AppConfig:
    """Retrieve the loaded configuration.

    Returns:
        AppConfig: The application configuration.

    Raises:
        RuntimeError: If configuration has not been loaded yet.
    """
    if _config is None:
        raise RuntimeError("Configuration not loaded. Call loadConfig() first.")
    return _config

