import random
import string

#  генерация рандомной строки
def generate_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

#  генерация рандомного пользователя
def generate_random_user_body() -> dict:
    return {
        "email": f"{generate_random_string(10)}@random.com",
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }