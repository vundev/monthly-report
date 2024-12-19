from typing import Annotated, Callable
from .tenant_repository import TenantRepository
from fastapi import Depends


TenantRepositoryDep = Annotated[TenantRepository, Depends()]
