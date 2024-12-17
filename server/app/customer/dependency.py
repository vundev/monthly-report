from typing import Annotated
from .customer_repository import CustomerRepository
from fastapi import Depends


CustomerRepositoryDep = Annotated[CustomerRepository, Depends()]
