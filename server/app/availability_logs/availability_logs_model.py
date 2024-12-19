from pydantic import BaseModel
from enum import Enum


class AvailabilityLevel(str, Enum):
    DEFAULT = "Default"
    CUSTOMER_SPECIFIC = "Customer-Specific"
    EXPIRED = "Expired"


class CreateAvailabilityLogMessageSpec(BaseModel):
    tenant_id: int
    level: AvailabilityLevel
