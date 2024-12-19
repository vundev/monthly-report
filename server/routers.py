from fastapi import APIRouter
from .controllers import customer_controller, tenant_controller, availability_logs_controller

apiRouter = APIRouter()
apiRouter.include_router(customer_controller.router)
apiRouter.include_router(tenant_controller.router)
apiRouter.include_router(availability_logs_controller.router)
