from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from ..settings.dependency import get_settings
from sqlmodel import SQLModel
from typing import AsyncGenerator

engine = create_async_engine(get_settings().database_uri, echo=True)
async_session_factory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db():
    async with engine.begin() as connection:
        # Create all tables in the database
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


async def dispose_db():
    await engine.dispose()
