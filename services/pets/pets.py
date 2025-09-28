import requests
from helper import Helper
from .endpoints import Endpoints
from .payloads import Payloads


class Pets(Helper):

    __endpoints = Endpoints
    payloads = Payloads

    host = "https://petstore.swagger.io/v2"

    def create_pet(self, payloads: dict):
        res = requests.post(
            url=f"{self.host}{self.__endpoints.post_pet}",
            headers=self.headers,
            json=payloads,
        )

        assert res.status_code == 200
        return res.json()
