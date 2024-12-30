import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from server.app.customer.customer_repository import CustomerRepository
from server.app.customer.customer_schema import Customer
from sqlmodel import text
from server.services.query_service import QueryService
from pytest import raises
import asyncio
from fastapi import HTTPException, status


@pytest.fixture
def repository(session: AsyncSession):
    return CustomerRepository(session=session)


class TestCustomerRepository:
    FIRST_CUSTOMER_QUERY = text("SELECT * FROM customer LIMIT 1;")

    async def test_create_customer(self,
                                   repository: CustomerRepository, session: AsyncSession):
        src_customer = await repository.create_customer("test@mail.com", "password_hash")
        assert src_customer.customer_name == "test@mail.com"
        assert src_customer.password_hash == "password_hash"

        customers_result = await session.execute(self.FIRST_CUSTOMER_QUERY)
        target_customer = Customer(**QueryService.to_dict(customers_result)[0])

        assert src_customer.customer_name == target_customer.customer_name
        assert src_customer.password_hash == target_customer.password_hash

    async def test_duplicate_customer(
            self, repository: CustomerRepository):
        customer = await repository.create_customer("test@mail.com", "password_hash")
        assert customer.customer_name == "test@mail.com"
        assert customer.password_hash == "password_hash"

        with raises(IntegrityError) as exception_info:
            await repository.create_customer(customer.customer_name,
                                             customer.password_hash)
            print(exception_info)

        assert exception_info.typename == "IntegrityError"

    async def test_find_customer(cls, repository: CustomerRepository):
        # Do not create in parallel since we use the same db session to commit 2
        # transactions. It is not possible to start another transaction while the previous
        # is still in progress with the same session, we have to use separate sessions or
        # just to run sequentially the create calls.
        await repository.create_customer("test1@mail.com", "password_hash"),
        await repository.create_customer("test2@mail.com", "password_hash")
        (customer1, customer2) = await asyncio.gather(repository.find_customer_by_name("test1@mail.com"),
                                                      repository.find_customer_by_name("test2@mail.com"))

        assert customer1.customer_name == "test1@mail.com"
        assert customer2.customer_name == "test2@mail.com"

    async def test_find_non_existing_customer(cls, repository: CustomerRepository):
        with raises(HTTPException) as exception_info:
            await repository.find_customer_by_name("non existing customer")

        assert exception_info.value.status_code == status.HTTP_404_NOT_FOUND
