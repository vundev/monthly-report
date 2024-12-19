from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from ..tenant.tenant_schema import Tenant
from sqlalchemy import CheckConstraint


class AvailabilityLogs(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tenant_id: int = Field(foreign_key="tenant.id")
    log_date: date
    availability_level: str = Field(nullable=False)

    __table_args__ = (
        CheckConstraint(
            "availability_level IN ('Default', 'Customer-Specific', 'Expired')",
            name="check_availability_level"
        ),
    )

    tenant: Tenant = Relationship(back_populates="logs")
