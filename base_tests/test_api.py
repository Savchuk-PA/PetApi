from pprint import pprint

import services


class TestPets:

    def test_create_pet(self):
        pets = services.Pets()
        res = pets.create_pet(payloads=pets.payloads.test_pet)
        # test_pet = {
        #     "id": 900,
        #     "name": "Маркиз",
        #     "category": {"id": 1, "name": "cat"},
        #     "photoUrls": ["https://example.com/photo.jpg"],
        #     "tags": [{"id": 2, "name": "big_cat"}],
        #     "status": "available",
        #

        ex_cat_id = 900
        ex_name_pet = "Маркиз"
        ex_category_id = 1
        ex_category_name = "cat"
        ex_tags_id = 2
        ex_tags_name = "big_cat"
        ex_status = "available"
        assert res["id"] == ex_cat_id
        assert res["name"] == ex_name_pet
        assert res["category"]["id"] == ex_category_id
        assert res["category"]["name"] == ex_category_name
        assert res["tags"][0]["id"] == ex_tags_id
        assert res["tags"][0]["name"] == ex_tags_name
        assert res["status"] == ex_status
