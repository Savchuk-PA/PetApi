from pprint import pprint
import allure
import pytest

import services

from services.pets.payloads import positive_cases


class TestPets:

    @allure.issue("https://sadasd.com", "Название задачи в джира")
    @pytest.mark.parametrize("payloads", positive_cases)
    @pytest.mark.asyncio
    async def test_create_pet(self, payloads, async_client):
        pets = services.Pets(async_client=async_client)
        res = await pets.create_pet(payloads=payloads)
        assert res.id == payloads["id"]
        assert res.name == payloads["name"]
        assert res.category.id == payloads["category"]["id"]
        assert res.category.name == payloads["category"]["name"]
        assert res.tags[0].id == payloads["tags"][0]["id"]
        assert res.tags[0].name == payloads["tags"][0]["name"]
        assert res.status == payloads["status"]

    @pytest.mark.asyncio
    async def test_get_pet_by_id(self, pet, async_client):
        pets = services.Pets(async_client=async_client)
        res = await pets.get_pet_by_id(pet_id=pet.id)
        pprint(res)
