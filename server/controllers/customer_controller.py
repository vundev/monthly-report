from fastapi_utils.cbv import cbv
from fastapi import APIRouter
from ..app.customer.dependency import CustomerRepositoryDep, CustomerDep
from ..app.customer.customer_model import CustomerCredentials
from ..security.dependency import PasswordContextDep, CustomerFormDataDep, TokenServiceDep
from fastapi import HTTPException, status

router = APIRouter(prefix="/customer")


@cbv(router=router)
class CustomerController:

    def __init__(self,
                 customer_repository: CustomerRepositoryDep,
                 password_context: PasswordContextDep,
                 token_service: TokenServiceDep):
        self.customer_repository = customer_repository
        self.password_context = password_context
        self.token_service = token_service

    @router.post("/register")
    async def register_customer(self,
                                customer_credentials: CustomerCredentials):
        customer = await self.customer_repository.create_customer(
            customer_name=customer_credentials.username,
            password_hash=self.password_context.hash(customer_credentials.password))
        return self.token_service.create_token(customer_name=customer.customer_name)

    @router.post("/access-token")
    async def log_in(self, form_data: CustomerFormDataDep):
        customer = await self._authenticate_customer(
            customer_name=form_data.username, password=form_data.password)
        return self.token_service.create_token(customer_name=customer.customer_name)

    @router.get("/me")
    async def get_customer(self, customer: CustomerDep):
        return customer

    async def _authenticate_customer(self,
                                     customer_name: str,
                                     password: str):
        customer = await self.customer_repository.find_customer_by_name(
            customer_name=customer_name)

        if not self._is_password_valid(password, customer.password_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
        return customer

    def _is_password_valid(self, password: str, password_hash: str):
        return self.password_context.verify(password, password_hash)
