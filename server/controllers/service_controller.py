from fastapi_utils.cbv import cbv
from fastapi import APIRouter
from ..database.dependency import SessionDep
from sqlmodel import select
from ..app.service.service_schema import Service
from ..app.service.service_model import ServiceInfo

router = APIRouter(prefix="/service")


@cbv(router=router)
class ServiceController:

    @router.get("/list", response_model=list[ServiceInfo])
    async def get_service_names(self, session: SessionDep):
        serviceQuery = select(Service)
        result = await session.execute(serviceQuery)
        services = result.scalars().all()
        return services
