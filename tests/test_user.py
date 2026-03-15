import allure
from api_client import BurgerApiClient

@allure.feature("User")
class TestUser:
    @allure.title("Создать уникального пользователя")
    def test_create_user_success(self, user_data):
        res = BurgerApiClient.register_user(user_data)
        assert res.status_code == 200
        assert res.json()["success"] is True
        BurgerApiClient.delete_user(res.json().get("accessToken"))

    @allure.title("Создать дубликат пользователя")
    def test_create_duplicate_user(self, created_user):
        _, data = created_user
        res = BurgerApiClient.register_user(data)
        assert res.status_code == 403
        assert res.json()["message"] == "User already exists"

    @allure.title("Создать пользователя без email")
    def test_create_user_no_field(self):
        res = BurgerApiClient.register_user({"password": "123", "name": "Ivan"})
        assert res.status_code == 403
        assert "required fields" in res.json()["message"]

    @allure.title("Логин существующим пользователем")
    def test_login_success(self, created_user):
        _, data = created_user
        res = BurgerApiClient.login_user({"email": data["email"], "password": data["password"]})
        assert res.status_code == 200

    @allure.title("Логин с неверными данными")
    def test_login_wrong_creds(self):
        res = BurgerApiClient.login_user({"email": "fail@ya.ru", "password": "000"})
        assert res.status_code == 401