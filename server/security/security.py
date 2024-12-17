from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="customer/access-token")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def validate_customer_form_data(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username.strip()
    password = form_data.password

    _validate_customer_data(customer_name=username, password=password)

    form_data.username = username

    return form_data


def _validate_customer_data(customer_name: str, password: str):
    if not customer_name or not customer_name.strip():
        raise ValueError("Customer name cannot be empty or whitespace.")
    if not password or len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
