from server.database.dependency import SessionDep
from .tenant_schema import Tenant
import datetime
from .raw_queries import *
from server.services.dependency import QueryServiceDep, DateServiceDep


class TenantRepository:
    def __init__(self,
                 session: SessionDep,
                 query_service: QueryServiceDep,
                 date_service: DateServiceDep):
        self.session = session
        self.query_service = query_service
        self.date_service = date_service

    async def create_tenant(self,
                            customer_id: int,
                            service_id: int,
                            email: str):
        tenant = Tenant(customer_id=customer_id,
                        service_id=service_id,
                        email=email,
                        date_of_expiration=self.date_service.get_next_month_beginning())
        self.session.add(tenant)
        await self.session.commit()
        await self.session.refresh(tenant)
        return tenant

    async def list_tenant_infos(self, customer_id: int):
        tenantInfoRows = await self.session.execute(
            query_tenant_infos, {"customer_id": customer_id}
        )

        return self.query_service.to_dict(tenantInfoRows)
