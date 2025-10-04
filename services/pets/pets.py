import allure
import requests
import logging


from helper import Helper
from .endpoints import Endpoints
from .payloads import Payloads
from .models.pet_model import PetModelResponse

logger = logging.getLogger(__name__)


class Pets(Helper):

    __endpoints = Endpoints
    payloads = Payloads

    @allure.step("Create Pet")
    def create_pet(
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
        response = requests.post(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )
        return self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    def get_pet_by_id(self, pet_id: int, status_code: int):
        """
        Получить питомца по ID
        :param pet_id: ID питомца
        :param status_code: status code for checking response
        :return: PetModelResponse
        """
        response = requests.get(
            url=f"{self.host}{self.__endpoints.pet_by_id(pet_id=pet_id)}",
            headers=self.headers,
        )

        return self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    def update_pet(
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
        response = requests.get(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )
        return self.basic_assert_response(
            response=response, pydantic_model=PetModelResponse, status_code=status_code
        )

    def delete_pet(self, pet_id: int):
        """
        Удаление питомца по ID
        :param pet_id: ID питомца
        :return: None
        """
        res = requests.delete(
            url=f"{self.host}{self.__endpoints.pet_by_id(pet_id=pet_id)}",
            headers=self.headers,
        )
        assert res.status_code == 200
        return res.json()
