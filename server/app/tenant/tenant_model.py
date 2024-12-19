from pydantic import BaseModel, model_validator, Field
from fastapi import HTTPException, status
from datetime import date


class CreateTenantSpec(BaseModel):
    email: str
    service_id: int


class TenantInfo(BaseModel):
    service_name: str
    email: str
    date_of_expiration: date
