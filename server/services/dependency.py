from typing import Annotated
from .query_service import QueryService
from fastapi import Depends

QueryServiceDep = Annotated[QueryService, Depends()]
