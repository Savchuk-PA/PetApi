import pytest

import services


@pytest.fixture
def pet():
    pets = services.Pets()
    res = pets.create_pet(payloads=pets.payloads.test_pet)
    yield res
    pets.delete_pet(pet_id=res["id"])
