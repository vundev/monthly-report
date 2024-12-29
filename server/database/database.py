from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from ..settings.dependency import get_settings
from sqlmodel import SQLModel
from typing import AsyncGenerator

engine = None
async_session_factory = None


async def create_db():
    global engine, async_session_factory

    engine = create_async_engine(get_settings().database_uri, echo=True)
    async_session_factory = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with engine.begin() as connection:
        # Create all tables in the database
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    global async_session_factory

    async with async_session_factory() as session:
        yield session


async def dispose_db():
    global engine

    await engine.dispose()
