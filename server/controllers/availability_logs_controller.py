from fastapi_utils.cbv import cbv
from fastapi import APIRouter
from ..app.availability_logs.dependency import AvailabilityLogsRepositoryDep
from ..app.availability_logs.availability_logs_model import CreateAvailabilityLogMessageSpec, TenantSlaInfo, ReportItem
from ..app.customer.dependency import CustomerDep

router = APIRouter(prefix="/sla")


@cbv(router=router)
class AvailabilityLogsController:

    def __init__(self,
                 availability_logs_repository: AvailabilityLogsRepositoryDep,
                 # Restrict those endpoints only to authenticated users.
                 _: CustomerDep):
        self.availability_logs_repository = availability_logs_repository

    @router.post("/log")
    async def log_message(
            self, create_log_message_spec: CreateAvailabilityLogMessageSpec):
        await self.availability_logs_repository.crete_log_message(
            tenant_id=create_log_message_spec.tenant_id,
            level=create_log_message_spec.level)

    @router.get("/tenant-sla", response_model=list[TenantSlaInfo])
    async def list_tenant_sla_per_month(self):
        """
        Use for debug purpose.
        """
        return await self.availability_logs_repository.list_tenant_sla_per_month()

    @router.get("/report", response_model=list[ReportItem])
    async def get_report(self):
        return await self.availability_logs_repository.get_report()

    @router.get("/report-strict")
    async def get_report_strict(self):
        return await self.availability_logs_repository.get_report_strict()
