"""
Application configuration module.

Loads environment-based settings using Pydantic BaseSettings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    redis_host: str
    redis_port: int
    cache_ttl_seconds: int
    third_party_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


app_settings: Settings = Settings()  # type: ignore[call-arg]
