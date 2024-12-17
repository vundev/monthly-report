from pydantic import BaseModel, model_validator, Field
from fastapi import HTTPException, status


class CustomerCredentials(BaseModel):
    username: str
    password: str

    @model_validator(mode="after")
    def _validate(self):
        self._validate_username()
        self._validate_password()
        return self

    def _validate_username(self):
        if not self.username or not self.username.strip():
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Username cannot be empty or whitespace.")
        self.username = self.username.strip()
        return self

    def _validate_password(self):
        if not self.password or len(self.password) < 8:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Password must be at least 8 characters long.")
        return self


class CustomerMe(BaseModel):
    customer_name: str = Field(alias='customerName')
