from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(alias='accessToken')
    token_type: str = Field(alias='tokenType')

    class Config:
        populate_by_name = True

class TokenData(BaseModel):
    customer_name: str
