
from server.database.database import get_db_session
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
import pytest
from httpx import AsyncClient, ASGITransport
from server.main import app
from pytest import MonkeyPatch


# Use autouse to never have to explicitly define client in tests in order to be created.
@pytest.fixture(autouse=True)
async def client(monkeypatch: MonkeyPatch) -> AsyncGenerator[AsyncClient, None]:
    # Patch database uri env variable. For the tests we use in memory sqlite db.
    monkeypatch.setenv("DATABASE_URI", "sqlite+aiosqlite:///:memory:")

    # Migrate db.
    await app.router.startup()

    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as client:
        yield client

    await app.router.shutdown()


@pytest.fixture
async def session() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_db_session():
        yield session
