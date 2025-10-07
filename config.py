import logging


from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

# logging.basicConfig(
#     level=logging.INFO,  # Минимальный уровень, который будет сохраняться
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",  # Формат сообщения
#     datefmt="%Y-%m-%d %H:%M:%S",  # Формат даты/времени
#     handlers=[
#         logging.StreamHandler()
#     ],  # Вывод в консоль (можно заменить на FileHandler)
# )
#
# log = logging.getLogger(__name__)


class Api(BaseModel):

    host: str
    timeout: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    api: Api


settings = Settings()
