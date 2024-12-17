from sqlmodel import SQLModel, Field


class Service(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    service_name: str = Field(nullable=False, unique=True, index=True)
