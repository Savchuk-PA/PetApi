from pprint import pprint
import allure
import services


class TestPets:

    @allure.issue("https://sadasd.com", "Название задачи в джира")
    def test_create_pet(self):
        pets = services.Pets()
        res = pets.create_pet(payloads=pets.payloads.test_pet)
        ex_cat_id = 900
        ex_name_pet = "Маркиз"
        ex_category_id = 1
        ex_category_name = "cat"
        ex_tags_id = 2
        ex_tags_name = "big_cat"
        ex_status = "available"
        assert res.id == ex_cat_id
        assert res.name == ex_name_pet
        assert res.category.id == ex_category_id
        assert res.category.name == ex_category_name
        assert res.tags[0].id == ex_tags_id
        assert res.tags[0].name == ex_tags_name
        assert res.status == ex_status

    def test_get_pet_by_id(self, pet):
        pets = services.Pets()
        res = pets.get_pet_by_id(pet_id=pet.id)
        pprint(res)
