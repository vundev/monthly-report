from fastapi import APIRouter
from .controllers import customer_controller

apiRouter = APIRouter()
apiRouter.include_router(customer_controller.router)
