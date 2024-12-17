from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    customer_name: str = Field(nullable=False, unique=True, index=True)
    password_hash: str = Field(nullable=False)
