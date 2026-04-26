import pytest
from api_client import BurgerApiClient
from helpers import UserHelper

@pytest.fixture
def created_user():
    payload = UserHelper.generate_user_payload()
    response = BurgerApiClient.register_user(payload)
    token = response.json().get("accessToken")
    
    user_data = {"response": response, "payload": payload, "token": token}
    yield user_data
    
    if token:
        BurgerApiClient.delete_user(token)