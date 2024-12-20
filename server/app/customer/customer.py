from server.security.dependency import TokenDep, TokenServiceDep
from .customer_model import CustomerMe
from typing import Annotated
from .customer_repository import CustomerRepository
from fastapi import Depends

# --- Define here dependency resolvers. ---

async def get_authenticated_customer(token: TokenDep,
                                     # Can not import CustomerRepositoryDep since 
                                     # we will get circular import. That's why
                                     # we inject the repository manually. The Depends()
                                     # method grants that the same repository instance will be
                                     # used when an endpoint is hit for all dependencies that
                                     # use the CustomerRepository.
                                     customer_repository: Annotated[CustomerRepository, Depends()],
                                     token_service: TokenServiceDep):
    token_data = token_service.get_token_data(token=token)
    customer = await customer_repository.find_customer_by_name(
        customer_name=token_data.customer_name)
    # resource_model=CustomerMe does not work with alias, so create object explicitly.
    return CustomerMe(customerName=customer.customer_name,
                      customerId=customer.id)
