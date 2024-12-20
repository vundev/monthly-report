from pydantic import BaseModel


class ServiceInfo(BaseModel):
    service_name: str
    id: int
