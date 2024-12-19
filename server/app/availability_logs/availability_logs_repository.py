from server.database.dependency import SessionDep
from .availability_logs_schema import AvailabilityLogs
from datetime import datetime
from .availability_logs_model import AvailabilityLevel
from .raw_queries import query_tenant_sla, query_report, query_report_strict
from server.services.dependency import QueryServiceDep


class AvailabilityLogsRepository:
    def __init__(self,
                 session: SessionDep,
                 query_service: QueryServiceDep):
        self.session = session
        self.query_service = query_service

    async def crete_log_message(self, tenant_id: int, level: AvailabilityLevel):
        log_message = AvailabilityLogs(
            tenant_id=tenant_id,
            availability_level=level,
            log_date=datetime.now())

        self.session.add(log_message)
        await self.session.commit()
        await self.session.refresh(log_message)
        return log_message

    async def list_tenant_sla_per_month(self):
        tenant_sla_per_month = await self.session.execute(query_tenant_sla)
        return self.query_service.to_dict(tenant_sla_per_month)

    async def get_report(self):
        report = await self.session.execute(query_report)
        return self.query_service.to_dict(report)
    
    async def get_report_strict(self):
        report = await self.session.execute(query_report_strict)
        return self.query_service.to_dict(report)
