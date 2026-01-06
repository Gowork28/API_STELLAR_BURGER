class TestUserData:
    UserData = {
        "email": "anyainchina@yandex.com",
        "password": "ilovechina",
        "name": "anyainchina",
    }


#  Был заранее отправлен get-запрос на INGREDIENT_URL для получения существующего хеша ингредиентов
class TestIngredientData:
    IngredientData = {
        "ingredients": ["61c0c5a71d1f82001bdaaa7a", "61c0c5a71d1f82001bdaaa78" ]
    }


class Responses:
    OK_200 = {
        "status_code": 200
    }

    EXISTING_USER = {
        "status_code": 403,
        "success": False,
        "message": "User already exists"
    }

    USER_WITHOUT_ONE_FIELD = {
        "status_code": 403,
        "success": False,
        "message": "Email, password and name are required fields"
    }

    LOGIN_WITH_WRONG_DATA = {
        "status_code": 401,
        "success": False,
        "message": "email or password are incorrect"
    }

    ORDER_WITHOUT_INGREDIENTS = {
        "status_code": 400,
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    ORDER_WITH_WRONG_INGREDIENT_HASH = {
        "status_code": 500
    }