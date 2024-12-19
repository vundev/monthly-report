from typing import Annotated
from .query_service import QueryService
from .date_service import DateService
from fastapi import Depends

QueryServiceDep = Annotated[QueryService, Depends()]
DateServiceDep = Annotated[DateService, Depends()]
