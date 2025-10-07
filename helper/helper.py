import logging
from pprint import pprint
from typing import TypeVar, Type

import allure
from pydantic import BaseModel
from requests import Response

from config import settings

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class Helper:

    headers = {"Content-Type": "application/json"}
    host: str = settings.api.host

    @allure.step("Базовая проверка ответа от сервера:")
    async def basic_assert_response(
        self,
        response: Response,
        pydantic_model: Type[T],
        status_code: int = 200,
    ):
        try:
            logger.info("Response: status code %s", response.status_code)
            pprint(response.json())
            assert (
                response.status_code == status_code
            ), f"EX status code: {status_code}, AC status code: {response.status_code}"
            return pydantic_model(**response.json())
        except ValueError as exc:
            logger.error(f"Exc: {exc}")
            logger.error("Response body is not a valid JSON: %s", response.text)
            raise
