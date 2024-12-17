from server.database.dependency import SessionDep
from .customer_schema import Customer


class CustomerRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    async def create_customer(self, username: str, password: str):
        customer = Customer(customer_name=username, password_hash=password)
        self.session.add(customer)
        await self.session.commit()
        await self.session.refresh(customer)
