from sqlmodel import SQLModel, Field, Relationship
from typing import List


class Service(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    service_name: str = Field(nullable=False, unique=True, index=True)

    # Class Tenant not yet loaded => use forward referencing to avoid
    # circular imports
    tenants: List["Tenant"] = Relationship(back_populates="service")
