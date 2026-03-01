"""
Main FastAPI application entrypoint.

Initializes Redis, defines routes, and handles upstream API integration.
"""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import httpx
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException

from app.cache import RedisCache
from app.config import app_settings
from app.schemas import CachedResponse, RandomUserAPIResponse

logger = logging.getLogger(__name__)


# Lifespan setup - start and shutdown of app


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle startup and shutdown lifecycle events."""

    redis_client = redis.Redis(
        host=app_settings.redis_host,
        port=app_settings.redis_port,
        decode_responses=True,
        max_connections=20,
    )

    fastapi_app.state.cache = RedisCache(redis_client)

    yield
    await redis_client.aclose()


app = FastAPI(lifespan=lifespan, docs_url="/docs")


# fetch function


async def fetch_random_user() -> RandomUserAPIResponse:
    """Fetch users from third-party API and transform response."""

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(app_settings.third_party_url)

    if response.status_code != 200:
        logger.error("Upstream API failed: %s", response.text)
        raise HTTPException(status_code=502, detail="Upstream API Error")

    raw = response.json()

    users = [
        {
            "id": user["id"],
            "first_name": user["name"]["first"],
            "last_name": user["name"]["last"],
            "email": user["email"],
        }
        for user in raw["data"]["data"]
    ]

    transformed = {
        "statusCode": raw["statusCode"],
        "data": {"data": users},
    }

    return RandomUserAPIResponse.model_validate(transformed)


@app.get("/random-users", response_model=CachedResponse)
async def get_random_users() -> CachedResponse:
    """Return cached users or fetch from upstream if cache miss."""

    cache: RedisCache = app.state.cache

    cache_key = "random-users"

    cached = await cache.get(cache_key)

    if cached:
        validated = RandomUserAPIResponse.model_validate(cached)
        return CachedResponse(source="cache", data=validated)

    # cache miss

    # Fetch from API

    data = await fetch_random_user()

    # store in cache

    await cache.set(
        key=cache_key, value=data.model_dump(), ttl_seconds=app_settings.cache_ttl_seconds
    )
    # model dumps converts pydantic model to plain python dictionary.

    return CachedResponse(source="api", data=data)
