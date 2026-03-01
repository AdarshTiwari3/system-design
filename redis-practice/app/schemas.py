"""
Pydantic schemas for API responses and data transformation.
"""

from typing import Literal

from pydantic import BaseModel


class RandomUser(BaseModel):
    """Simplified user model returned by our API."""

    id: int
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None


class RandomUserResponseData(BaseModel):
    """Wrapper containing list of users."""

    data: list[RandomUser]


class RandomUserAPIResponse(BaseModel):
    """Top-level API response format."""

    statusCode: int
    data: RandomUserResponseData


class CachedResponse(BaseModel):
    """Final response returned by service."""

    source: Literal["api", "cache"]
    data: RandomUserAPIResponse
