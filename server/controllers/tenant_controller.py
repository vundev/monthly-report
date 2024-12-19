from fastapi_utils.cbv import cbv
from fastapi import APIRouter
from ..app.tenant.dependency import TenantRepositoryDep
from ..app.customer.dependency import CustomerDep
from ..app.tenant.tenant_model import CreateTenantSpec, TenantInfo

router = APIRouter(prefix="/tenant")


@cbv(router=router)
class TenantController:

    def __init__(self,
                 tenant_repository: TenantRepositoryDep,
                 customer: CustomerDep):
        self.tenant_repository = tenant_repository
        self.customer = customer

    @router.post("/create")
    async def register_tenant(self, create_tenant_spec: CreateTenantSpec):
        await self.tenant_repository.create_tenant(
            customer_id=self.customer.customer_id,
            service_id=create_tenant_spec.service_id,
            email=create_tenant_spec.email)

    @router.post("/list", response_model=list[TenantInfo])
    async def log_in(self):
        return await self.tenant_repository.list_tenant_infos(self.customer.customer_id)
