import requests
from data import Endpoints

class BurgerApiClient:
    
    @staticmethod
    def register_user(payload):
        return requests.post(Endpoints.REGISTER, json=payload)

    @staticmethod
    def login_user(payload):
        return requests.post(Endpoints.LOGIN, json=payload)

    @staticmethod
    def delete_user(token):
        return requests.delete(Endpoints.USER, headers={"Authorization": token})

    @staticmethod
    def get_ingredients():
        return requests.get(Endpoints.INGREDIENTS)

    @staticmethod
    def create_order(payload, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(Endpoints.ORDERS, json=payload, headers=headers)