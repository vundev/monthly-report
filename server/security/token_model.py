from pydantic import BaseModel


class Token(BaseModel):
    # Those keys are reserved by oath2 policy. If you change them with alias to
    # accessToken for example the swagger will not work.
    access_token: str
    token_type: str

    class Config:
        populate_by_name = True


class TokenData(BaseModel):
    customer_name: str
