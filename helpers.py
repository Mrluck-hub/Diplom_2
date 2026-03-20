import random
import string

class UserHelper:
    @staticmethod
    def generate_user_payload():
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return {
            "email": f"tester_{random_str}@yandex.ru",
            "password": f"pass_{random_str}",
            "name": f"Tester_{random_str}"
        }