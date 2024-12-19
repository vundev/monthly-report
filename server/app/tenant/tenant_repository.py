from server.database.dependency import SessionDep
from .tenant_schema import Tenant
import datetime
from .raw_queries import *
from server.services.dependency import QueryServiceDep


class TenantRepository:
    def __init__(self, session: SessionDep, query_service: QueryServiceDep):
        self.session = session
        self.query_service = query_service

    async def create_tenant(self,
                            customer_id: int,
                            service_id: int,
                            email: str):
        tenant = Tenant(customer_id=customer_id,
                        service_id=service_id,
                        email=email,
                        date_of_expiration=self._get_next_month_beginning())
        self.session.add(tenant)
        await self.session.commit()
        await self.session.refresh(tenant)
        return tenant

    async def list_tenant_infos(self, customer_id: int):
        tenantInfoRows = await self.session.execute(
            query_tenant_infos, {"customer_id": customer_id}
        )

        return self.query_service.to_dict(tenantInfoRows)

    @classmethod
    def _get_next_month_beginning(cls):
        # Step 1: Get the current date
        today = datetime.date.today()
        if today.month == 12:
            # If it's December, next month is January of the next year
            next_month = 1
            next_month_year = today.year + 1
        else:
            next_month = today.month + 1
            next_month_year = today.year

        # Step 3: Create the first day of the next month at 00:00:00
        return datetime.datetime(
            next_month_year, next_month, 1, 0, 0, 0)
