from typing import Annotated, Callable
from .customer_repository import CustomerRepository
from fastapi import Depends
from .customer_model import CustomerMe
from server.security.dependency import TokenDep, TokenServiceDep


CustomerRepositoryDep = Annotated[CustomerRepository, Depends()]


async def get_authenticated_customer(token: TokenDep,
                                     customer_repository: CustomerRepositoryDep,
                                     token_service: TokenServiceDep):
    token_data = token_service.get_token_data(token=token)
    customer = await customer_repository.find_customer_by_name(
        customer_name=token_data.customer_name)
    # resource_model=CustomerMe does not work with alias, so create object explicitly.
    return CustomerMe(customerName=customer.customer_name,
                      customerId=customer.id)
CustomerDep = Annotated[CustomerMe, Depends(get_authenticated_customer)]
