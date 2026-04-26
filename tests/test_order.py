import allure
from api_client import BurgerApiClient

@allure.feature("Orders")
class TestOrders:
    @allure.title("Создание заказа с авторизацией")
    def test_order_with_auth(self, created_user):
        token = created_user["token"]
        ing = BurgerApiClient.get_ingredients().json()["data"][0]["_id"]
        res = BurgerApiClient.create_order({"ingredients": [ing]}, token)
        assert res.status_code == 200
        assert res.json()["success"] is True

    @allure.title("Создание заказа БЕЗ авторизации")
    def test_order_no_auth(self):
        ing = BurgerApiClient.get_ingredients().json()["data"][0]["_id"]
        res = BurgerApiClient.create_order({"ingredients": [ing]})
        assert res.status_code == 200

    @allure.title("Создание заказа с ингредиентами")
    def test_order_with_ingredients(self, created_user):
        token = created_user["token"]
        ings = [i["_id"] for i in BurgerApiClient.get_ingredients().json()["data"][:2]]
        res = BurgerApiClient.create_order({"ingredients": ings}, token)
        assert res.status_code == 200

    @allure.title("Заказ без ингредиентов")
    def test_order_no_ing_fail(self, created_user):
        res = BurgerApiClient.create_order({"ingredients": []}, created_user["token"])
        assert res.status_code == 400
        assert res.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Заказ с неверным хешем")
    def test_order_bad_hash_fail(self, created_user):
        res = BurgerApiClient.create_order({"ingredients": ["not_a_hash"]}, created_user["token"])
        assert res.status_code == 500