from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Api(BaseModel):

    host: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    api: Api


settings = Settings()
