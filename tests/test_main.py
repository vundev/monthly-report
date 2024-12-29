import pytest
from server.app.service.service_schema import Service
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import inspect
from sqlmodel import Session
import asyncio
from typing import Callable
from sqlmodel import text


class TestMain:
    EXISTING_SERVICES = ["Web hosting",
                         "Netflix", "Apple developer memebership"]
    ONE_CUSTOMER_QUERY = text("SELECT 1 FROM customer LIMIT 1;")

    async def test_create_services(self, session: AsyncSession):
        result = await session.execute(select(Service))
        existing_services = result.scalars().all()
        assert [
            service.service_name for service in existing_services] == self.EXISTING_SERVICES

    async def test_are_tables_created(self, session: AsyncSession):
        # Use run_sync because inspection does not work with async.
        async with session.begin():
            return await asyncio.gather(
                session.run_sync(self._is_table_exists("Customer")),
                session.run_sync(self._is_table_exists("Service")))

    async def test_is_customers_table_empty(self, session: AsyncSession):
        result = await session.execute(self.ONE_CUSTOMER_QUERY)
        customer = result.fetchone()
        assert customer == None

    def _is_table_exists(self, table_name: str) -> bool:
        # lambda accepting the sync Session object.
        def _check(sync_session: Session) -> Callable[[Session], bool]:
            inspector = inspect(sync_session.bind)
            inspector.has_table(table_name)

        return _check
