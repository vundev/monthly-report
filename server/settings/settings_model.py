from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_uri: str
    # Type `openssl rand -hex 32` to generate
    secret_key: str
    token_alg: str
    token_exp_time: int
    token_type: str

    model_config = SettingsConfigDict(
        env_file="server/.env"
    )
