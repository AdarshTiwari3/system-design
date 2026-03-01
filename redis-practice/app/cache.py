"""
Redis cache abstraction layer.

Handles JSON serialization/deserialization and Redis operations.
"""

import json
import logging
from typing import Any

import redis.asyncio as redis

logger = logging.getLogger(__name__)


class RedisCache:
    """Async Redis cache wrapper with JSON serialization."""

    def __init__(self, client: redis.Redis) -> None:
        """Initialize Redis cache with async client."""
        self._client = client

    async def get(self, key: str) -> dict[str, Any] | None:
        """Retrieve cached JSON value by key."""

        try:
            value = await self._client.get(key)
        except redis.RedisError as exc:
            logger.warning("Redis GET failed for key=%s: %s", key, exc)
            return None

        if value is None:
            return None

        try:
            data = json.loads(value)
        except json.JSONDecodeError:
            logger.error("Invalid JSON in Redis for key=%s", key)
            return None

        if not isinstance(data, dict):
            logger.error("Cached value is not dict for key=%s", key)
            return None

        return data

    async def set(
        self,
        key: str,
        value: dict[str, Any],
        ttl_seconds: int,
    ) -> None:
        """Store dictionary value in Redis with TTL."""

        try:
            serialized = json.dumps(value)
            await self._client.setex(key, ttl_seconds, serialized)
        except redis.RedisError as exc:
            logger.warning("Redis SET failed for key=%s: %s", key, exc)

    async def delete(self, key: str) -> None:
        """Delete key from Redis."""

        try:
            await self._client.delete(key)
        except redis.RedisError as exc:
            logger.warning("Redis DELETE failed for key=%s: %s", key, exc)

    async def exists(self, key: str) -> bool:
        """Check if key exists in Redis."""

        try:
            return bool(await self._client.exists(key))
        except redis.RedisError:
            return False
