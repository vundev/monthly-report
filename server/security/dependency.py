from typing import Annotated
from fastapi import Depends
from passlib.context import CryptContext

from .token_service import TokenService
from .security import get_password_context, validate_customer_form_data, oauth2_scheme
from fastapi.security import OAuth2PasswordRequestForm

PasswordContextDep = Annotated[CryptContext, Depends(get_password_context)]
CustomerFormDataDep = Annotated[OAuth2PasswordRequestForm, Depends(
    validate_customer_form_data)]
TokenServiceDep = Annotated[TokenService, Depends()]
TokenDep = Annotated[str, Depends(oauth2_scheme)]
