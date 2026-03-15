import random
import string

BASE_URL = "https://stellarburgers.education-services.ru"

class Endpoints:
    REGISTER = f"{BASE_URL}/api/auth/register"
    LOGIN = f"{BASE_URL}/api/auth/login"
    USER = f"{BASE_URL}/api/auth/user"
    ORDERS = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"

def generate_user_payload():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "email": f"tester_{random_str}@yandex.ru",
        "password": f"pass_{random_str}",
        "name": f"Tester_{random_str}"
    }