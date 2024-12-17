from typing import Annotated
from .customer_repository import CustomerRepository
from fastapi import Depends
from .resolver import resolve_customer_repository


CustomerRepositoryDep = Annotated[CustomerRepository, Depends()]
