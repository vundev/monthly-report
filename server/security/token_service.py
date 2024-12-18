from datetime import timedelta, datetime, timezone
import jwt
from ..settings.dependency import SettingsDep
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError
from .token_model import TokenData, Token


class TokenService:
    def __init__(self, settings: SettingsDep):
        self.settings = settings

    def create_token(self, customer_name: str) -> Token:
        """Create a new token for a given customer name."""
        access_token = self._create_access_token(data={"sub": customer_name})
        return Token(access_token=access_token, token_type=self.settings.token_type)

    def get_token_data(self, token: str) -> TokenData:
        """Validate a token and return the customer name inside it."""
        invalid_token_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

        try:
            payload = jwt.decode(
                token, self.settings.secret_key, algorithms=[
                    self.settings.token_alg]
            )
            customer_name: str | None = payload.get("sub")
            if customer_name is None:
                raise invalid_token_exception
            return TokenData(customer_name=customer_name)
        except InvalidTokenError:
            raise invalid_token_exception

    def _create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        """Generate a new access token with an optional expiration time."""
        data_copy = data.copy()

        # Set expiration time
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + \
                timedelta(minutes=self.settings.token_exp_time)
        data_copy.update({"exp": expire})

        return jwt.encode(data_copy, self.settings.secret_key, algorithm=self.settings.token_alg)
