from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from ..customer.customer_schema import Customer
from ..service.service_schema import Service
from typing import List


class Tenant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_id: int | None = Field(foreign_key="service.id", nullable=True)
    customer_id: int | None = Field(foreign_key="customer.id", nullable=True)
    email: str = Field(max_length=255)
    date_of_expiration: date | None = None

    service: Service = Relationship(back_populates="tenants")
    customer: Customer = Relationship(back_populates="tenants")

    logs: List["AvailabilityLogs"] = Relationship(back_populates="tenant")
