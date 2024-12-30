
from fastapi import status
from server.main import app
from server.app.customer.customer_repository import CustomerRepository
from tests.controllers.test_customer_controller_mock import MockCustomerRepository, MockTokenService, MockCryptoContext
from httpx import AsyncClient
from server.security.token_service import TokenService
from pytest_mock import MockerFixture
import pytest
from unittest.mock import AsyncMock, ANY
from server.security.security import get_password_context, oauth2_scheme


@pytest.fixture
def create_customer_spy(mocker: MockerFixture):
    return mocker.spy(MockCustomerRepository, "create_customer")


class TestCustomerController:

    def setup_method(self):
        # Here we can not have race conditions, parallel tests overwrite dependencies
        # because for each test case we create a new app instance
        # (see the scope for the client fixture).
        app.dependency_overrides = {
            CustomerRepository: MockCustomerRepository,
            TokenService: MockTokenService,
            get_password_context: lambda: MockCryptoContext(),
            oauth2_scheme: lambda: "Token test@mail.com"
        }

    def teardown_method(self):
        app.dependency_overrides = {}

    async def test_register(self, client: AsyncClient, create_customer_spy: AsyncMock):
        token = await client.post("/customer/register", json={
            "username": "test@mail.com",
            "password": "password"
        })

        create_customer_spy.assert_awaited_once_with(
            ANY,
            customer_name="test@mail.com",
            password_hash="password_hash"
        )

        assert token.json() == {
            "access_token": "Token test@mail.com", "token_type": "test"}

    async def test_log_in_with_wrong_password(self, client: AsyncClient):
        reponse = await client.post("/customer/access-token", data={
            "username": "test@mail.com",
            "password": "wrong password"
        })

        assert reponse.status_code == status.HTTP_400_BAD_REQUEST

    async def test_log_in_success(self, client: AsyncClient):
        reponse = await client.post("/customer/access-token", data={
            "username": "test@mail.com",
            "password": "password"
        })

        assert reponse.json() == {
            "access_token": "Token test@mail.com", "token_type": "test"}

    async def test_get_customer(self, client: AsyncClient):
        customer_me = await client.get("/customer/me")

        assert customer_me.json() == {
            "customerName": "test@mail.com", "customerId": 1}
