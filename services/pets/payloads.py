import random
from faker import Faker

fake = Faker("ru_Ru")


class Payloads:

    test_pet = {
        "id": 900,
        "name": "Маркиз",
        "category": {"id": 1, "name": "cat"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 2, "name": "big_cat"}],
        "status": "available",
    }
    test_pet_2 = {
        "id": 901,
        "name": "Барсик",
        "category": {"id": 2, "name": "cat"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 3, "name": "mini_cat"}],
        "status": "available",
    }
    test_pet_3 = {
        "id": 902,
        "name": "Васька",
        "category": {"id": 2, "name": "cat"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 3, "name": "mini_cat"}],
        "status": "available",
    }
    test_pet_4 = {
        "id": 903,
        "name": "Адский_кот",
        "category": {"id": 2, "name": "cat"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 3, "name": "mini_cat"}],
        "status": "available",
    }


positive_cases = (
    Payloads.test_pet,
    Payloads.test_pet_2,
    Payloads.test_pet_3,
)
