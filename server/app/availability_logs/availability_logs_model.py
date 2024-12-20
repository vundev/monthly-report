from pydantic import BaseModel
from enum import Enum
from datetime import date


class AvailabilityLevel(str, Enum):
    DEFAULT = "Default"
    CUSTOMER_SPECIFIC = "Customer-Specific"
    EXPIRED = "Expired"


class CreateAvailabilityLogMessageSpec(BaseModel):
    tenant_id: int
    level: AvailabilityLevel


class TenantSlaInfo(BaseModel):
    month: str
    tenant_id: int
    email: str
    service_name: str
    min_availability_level: int
    expired_count: int


class ReportItem(BaseModel):
    month: str
    customer_name: str
    email: str
    service_name: str
    availability_level: str
