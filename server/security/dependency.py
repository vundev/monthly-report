from typing import Annotated
from fastapi import Depends
from passlib.context import CryptContext

from .token_service import TokenService
from .security import password_context, validate_customer_form_data
from fastapi.security import OAuth2PasswordRequestForm

PasswordContextDep = Annotated[CryptContext, Depends(lambda: password_context)]
CustomerFormDataDep = Annotated[OAuth2PasswordRequestForm, Depends(
    validate_customer_form_data)]
TokenServiceDep = Annotated[TokenService, Depends()]
