import allure
from api_client import BurgerApiClient
from helpers import UserHelper

@allure.feature("User")
class TestUser:
    @allure.title("Создать уникального пользователя")
    def test_create_user_success(self):
        payload = UserHelper.generate_user_payload()
        res = BurgerApiClient.register_user(payload)
        assert res.status_code == 200
        assert res.json()["success"] is True
        BurgerApiClient.delete_user(res.json().get("accessToken"))

    @allure.title("Создать дубликат пользователя")
    def test_create_duplicate_user(self, created_user):
        payload = created_user["payload"]
        res = BurgerApiClient.register_user(payload)
        assert res.status_code == 403
        assert res.json()["message"] == "User already exists"

    @allure.title("Создать пользователя без email")
    def test_create_user_no_field(self):
        payload = UserHelper.generate_user_payload()
        payload.pop("email")
        res = BurgerApiClient.register_user(payload)
        assert res.status_code == 403
        assert "required fields" in res.json()["message"]

    @allure.title("Логин существующим пользователем")
    def test_login_success(self, created_user):
        payload = created_user["payload"]
        res = BurgerApiClient.login_user({"email": payload["email"], "password": payload["password"]})
        assert res.status_code == 200

    @allure.title("Логин с неверными данными")
    def test_login_wrong_creds(self,created_user):
        payload = created_user["payload"]
        res = BurgerApiClient.login_user({"email": payload["email"], "password": "000"})
        assert res.status_code == 401