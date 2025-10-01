import requests
from helper import Helper
from .endpoints import Endpoints
from .payloads import Payloads
from .models.pet_model import PetModelResponse


class Pets(Helper):

    __endpoints = Endpoints
    payloads = Payloads

    def create_pet(self, payloads: dict) -> PetModelResponse:
        """
        Create a new pet
        :param payloads: dict obj description
        :return: dict
        """
        res = requests.post(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )

        assert res.status_code == 200
        return PetModelResponse(**res.json())

    def get_pet_by_id(self, pet_id: int):
        """
        Получить питомца по ID
        :param pet_id: ID питомца
        :return: pet obj
        """
        res = requests.get(
            url=f"{self.host}{self.__endpoints.pet_by_id(pet_id=pet_id)}",
            headers=self.headers,
        )
        assert res.status_code == 200
        return PetModelResponse(**res.json())

    def update_pet(self, payloads: dict):
        """
        Обновление питомца по ID
        :param payloads: dict с параметрами питомца
        :return: новое описание объекта в json
        """
        res = requests.get(
            url=f"{self.host}{self.__endpoints.pet}",
            headers=self.headers,
            json=payloads,
        )
        assert res.status_code == 200
        return PetModelResponse(**res.json())

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
