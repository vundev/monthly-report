from server.app.customer.customer_schema import Customer
from server.security.token_model import Token, TokenData
import re


class MockCustomerRepository:
    async def create_customer(self,
                              customer_name: str,
                              password_hash: str):
        return Customer(customer_name=customer_name, password_hash=password_hash)

    async def find_customer_by_name(self, customer_name: str):
        return Customer(customer_name=customer_name, password_hash="password_hash", id=1)


class MockTokenService:
    def create_token(self, customer_name: str):
        return Token(access_token=f"Token {customer_name}",
                     token_type="test")

    def get_token_data(self, token: str):
        match = re.match(r"Token (.+)", token)
        return TokenData(customer_name=match.group(1) if match else "")


class MockCryptoContext:
    def hash(self, password: str):
        return "password_hash"

    def verify(self, password: str, password_hash: str):
        return password == "password"
