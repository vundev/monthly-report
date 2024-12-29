
from server.database.database import get_db_session
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
import pytest
from httpx import AsyncClient, ASGITransport
from server.main import app
from pytest import MonkeyPatch


@pytest.fixture(scope="session")
def monkeymodule():
    """
    Expose monkeypatch in scope session fixtures.
    """
    from _pytest.monkeypatch import MonkeyPatch
    monkey_patch = MonkeyPatch()
    yield monkey_patch
    monkey_patch.undo()


# Use autouse to never have to explicitly define client in tests in order to be created.
@pytest.fixture(scope="session", autouse=True)
async def client(monkeymodule: MonkeyPatch) -> AsyncGenerator[AsyncClient, None]:
    # Patch database uri env variable. For the tests we use in memory sqlite db.
    monkeymodule.setenv("DATABASE_URI", "sqlite+aiosqlite:///:memory:")

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
