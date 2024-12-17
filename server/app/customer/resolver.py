from .customer_repository import CustomerRepository
from server.database.dependency import SessionDep


def resolve_customer_repository(session: SessionDep):
    return CustomerRepository(session=session)
