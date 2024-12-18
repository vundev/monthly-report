from sqlmodel import SQLModel, Field, Relationship
from typing import List


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    customer_name: str = Field(nullable=False, unique=True, index=True)
    password_hash: str = Field(nullable=False)

    # Class Tenant not yet loaded => use forward referencing to avoid
    # circular imports
    tenants: List["Tenant"] = Relationship(back_populates="customer")
