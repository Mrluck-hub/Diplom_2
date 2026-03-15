import pytest
from api_client import BurgerApiClient
from data import generate_user_payload

@pytest.fixture
def user_data():
    return generate_user_payload()

@pytest.fixture
def created_user(user_data):
    # Создаем через клиент
    response = BurgerApiClient.register_user(user_data)
    token = response.json().get("accessToken")
    
    yield response, user_data
    
    # Удаляем через клиент после теста
    if token:
        BurgerApiClient.delete_user(token)