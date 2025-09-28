import random
from faker import Faker

fake = Faker("ru_Ru")
print(fake.name())


class Payloads:

    # pet_data = {
    #     "id": random.randint(1, 100),
    #     "name": fake.name(),
    #     "category": {"id": random.randint(1, 10), "name": "cat"},
    #     "photoUrls": ["https://example.com/photo.jpg"],
    #     "tags": [{"id": random.randint(1, 10), "name": "big_cat"}],
    #     "status": "available",
    # }
    test_pet = {
        "id": 900,
        "name": "Маркиз",
        "category": {"id": 1, "name": "cat"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 2, "name": "big_cat"}],
        "status": "available",
    }
