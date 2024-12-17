from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str
    password_hash: str
