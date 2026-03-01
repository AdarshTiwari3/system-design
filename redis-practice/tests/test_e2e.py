import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_e2e_cache_flow() -> None:
    async with LifespanManager(app):
        transport = ASGITransport(app=app)

        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:

            first = await client.get("/random-users")
            second = await client.get("/random-users")

            assert first.status_code == 200
            assert second.status_code == 200

            assert first.json()["source"] in ["api", "cache"]
            assert second.json()["source"] == "cache"
