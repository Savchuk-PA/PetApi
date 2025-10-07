import time
from idlelib.window import add_windows_to_menu

import allure
import requests
import logging

from httpx import AsyncClient

from helper.base_client import BaseClient
from .endpoints import Endpoints
from .payloads import Payloads
from .models.pet_model import PetModelResponse

logger = logging.getLogger(__name__)


class Pets(BaseClient):

    __endpoints = Endpoints
    payloads = Payloads

    def __init__(self, async_client: AsyncClient):
        super().__init__(async_client=async_client)

    @allure.step("Create Pet")
    async def create_pet(
        self,
        payloads: dict,
        status_code: int = 200,
    ) -> PetModelResponse:
        """
        Create a new pet
        :param payloads: dict obj description
        :param status_code: status code for checking response
        :return: PetModelResponse
        """
        logger.info(f"Create pet: {payloads}")
        response = await self.post(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )
        return await self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    async def get_pet_by_id(self, pet_id: int, status_code: int = 200):
        """
        Получить питомца по ID
        :param pet_id: ID питомца
        :param status_code: status code for checking response
        :return: PetModelResponse
        """
        response = await self.get(
            url=f"{self.host}{self.__endpoints.pet_by_id(pet_id=pet_id)}",
            headers=self.headers,
        )

        return await self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    async def update_pet(
        self,
        payloads: dict,
        status_code: int,
    ):
        """
        Обновление питомца по ID
        :param payloads: dict с параметрами питомца
        :param status_code: status code for checking response
        :return: PetModelResponse
        """
        response = await self.get(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )
        return await self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    async def delete_pet(self, pet_id: int):
        """
        Удаление питомца по ID
        :param pet_id: ID питомца
        :return: None
        """
        response = await self.delete(
            url=f"{self.host}{self.__endpoints.pet_by_id(pet_id=pet_id)}",
            headers=self.headers,
        )
        assert response.status_code == 200
        return response.json()
