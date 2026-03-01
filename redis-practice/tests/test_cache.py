"""
Unit tests for RedisCache abstraction.
"""

from unittest.mock import AsyncMock

import pytest
from redis.exceptions import RedisError

from app.cache import RedisCache

# ----------------------
# GET TESTS
# ----------------------


@pytest.mark.asyncio
async def test_get_returns_dict_when_valid_json() -> None:
    mock_client = AsyncMock()
    mock_client.get.return_value = '{"name": "andy"}'

    cache = RedisCache(mock_client)

    result = await cache.get("test-key")

    assert result == {"name": "andy"}


@pytest.mark.asyncio
async def test_get_returns_none_when_key_missing() -> None:
    mock_client = AsyncMock()
    mock_client.get.return_value = None

    cache = RedisCache(mock_client)

    result = await cache.get("missing-key")

    assert result is None


@pytest.mark.asyncio
async def test_get_returns_none_when_invalid_json() -> None:
    mock_client = AsyncMock()
    mock_client.get.return_value = "not-valid-json"

    cache = RedisCache(mock_client)

    result = await cache.get("bad-json")

    assert result is None


@pytest.mark.asyncio
async def test_get_returns_none_when_json_not_dict() -> None:
    mock_client = AsyncMock()
    mock_client.get.return_value = '["list", "not", "dict"]'

    cache = RedisCache(mock_client)

    result = await cache.get("list-json")

    assert result is None


@pytest.mark.asyncio
async def test_get_returns_none_on_redis_error() -> None:
    mock_client = AsyncMock()
    mock_client.get.side_effect = RedisError("Redis down")

    cache = RedisCache(mock_client)

    result = await cache.get("error-key")

    assert result is None


# ----------------------
# SET TESTS
# ----------------------


@pytest.mark.asyncio
async def test_set_calls_setex_with_correct_arguments() -> None:
    mock_client = AsyncMock()

    cache = RedisCache(mock_client)

    await cache.set("key", {"a": 1}, ttl_seconds=60)

    mock_client.setex.assert_called_once()


@pytest.mark.asyncio
async def test_set_handles_redis_error() -> None:
    mock_client = AsyncMock()
    mock_client.setex.side_effect = RedisError("Write failed")

    cache = RedisCache(mock_client)

    # Should not raise
    await cache.set("key", {"a": 1}, ttl_seconds=60)


# ----------------------
# DELETE TESTS
# ----------------------


@pytest.mark.asyncio
async def test_delete_calls_redis_delete() -> None:
    mock_client = AsyncMock()

    cache = RedisCache(mock_client)

    await cache.delete("key")

    mock_client.delete.assert_called_once_with("key")


@pytest.mark.asyncio
async def test_delete_handles_redis_error() -> None:
    mock_client = AsyncMock()
    mock_client.delete.side_effect = RedisError("Delete failed")

    cache = RedisCache(mock_client)

    # Should not raise
    await cache.delete("key")


# ----------------------
# EXISTS TESTS
# ----------------------


@pytest.mark.asyncio
async def test_exists_returns_true_when_key_exists() -> None:
    mock_client = AsyncMock()
    mock_client.exists.return_value = 1

    cache = RedisCache(mock_client)

    result = await cache.exists("key")

    assert result is True


@pytest.mark.asyncio
async def test_exists_returns_false_when_key_missing() -> None:
    mock_client = AsyncMock()
    mock_client.exists.return_value = 0

    cache = RedisCache(mock_client)

    result = await cache.exists("key")

    assert result is False


@pytest.mark.asyncio
async def test_exists_returns_false_on_redis_error() -> None:
    mock_client = AsyncMock()
    mock_client.exists.side_effect = RedisError("Error")

    cache = RedisCache(mock_client)

    result = await cache.exists("key")

    assert result is False
