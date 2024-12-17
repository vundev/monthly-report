from server.database.dependency import SessionDep
from .customer_schema import Customer
from sqlmodel import select
from fastapi import HTTPException, status


class CustomerRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    async def create_customer(self, customer_name: str, password_hash: str):
        customer = Customer(customer_name=customer_name,
                            password_hash=password_hash)
        self.session.add(customer)
        await self.session.commit()
        await self.session.refresh(customer)
        return customer

    async def find_customer_by_name(self, customer_name: str):
        customerQuery = select(Customer).where(
            Customer.customer_name == customer_name)
        result = await self.session.execute(customerQuery)
        customer = result.scalar()
        if customer:
            return customer
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Customer not found")
