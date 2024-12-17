from fastapi_utils.cbv import cbv
from fastapi import APIRouter
from ..app.customer.dependency import CustomerRepositoryDep
from ..app.customer.customer_model import CustomerCredentials

router = APIRouter(prefix="/customer")


@cbv(router=router)
class CustomerController:

    def __init__(self, customer_repository: CustomerRepositoryDep):
        self.customer_repository = customer_repository

    @router.post("/register")
    async def register_customer(self, customer_credentials: CustomerCredentials):
        pass

    @router.get("/me")
    async def get_customer(self):
        return "me"
