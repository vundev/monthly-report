from typing import Annotated
from .customer_repository import CustomerRepository
from fastapi import Depends
from .customer_model import CustomerMe
from .customer import get_authenticated_customer


CustomerRepositoryDep = Annotated[CustomerRepository, Depends()]
CustomerDep = Annotated[CustomerMe, Depends(get_authenticated_customer)]
