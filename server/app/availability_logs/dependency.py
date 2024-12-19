from typing import Annotated
from .availability_logs_repository import AvailabilityLogsRepository
from fastapi import Depends


AvailabilityLogsRepositoryDep = Annotated[AvailabilityLogsRepository, Depends(
)]
