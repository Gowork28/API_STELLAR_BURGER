import allure
import pytest

from data.test_data import Responses, TestUserData
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title("Код 200 при успешном создании уникального пользователя")
    def test_create_user_success(self, unique_user):
        with allure.step("Создаем уникального пользователя"):
            response = UserMethods.create_user(body = unique_user)
            assert response.status_code == Responses.OK_200["status_code"]
            assert response.json()["success"] == True


    @allure.title("Код 400 при создании уникального пользователя, который уже зарегестрирован")
    def test_create_existing_user_fail(self, exist_user):
        with allure.step("Передаем в тест данные ранее зарегестированного пользователя"):
            user = exist_user
            response = UserMethods.create_user(body = user)
            assert response.status_code == Responses.EXISTING_USER["status_code"]
            assert response.json()["success"] == Responses.EXISTING_USER["success"]
            assert response.json()["message"] == Responses.EXISTING_USER["message"]


    @pytest.mark.parametrize("key,value", [
        ("email", ""),
        ("password", ""),
        ("name", "")
    ])
    @allure.title("Код 403 при создании уникального пользователя без одного из обязательных полей")
    def test_create_user_without_requirement_field_fail(self, key, value):
        with allure.step(f"Создаем пользователя с пустым полем {key}"):
            user = TestUserData.UserData.copy()
            user[key] = value
            response = UserMethods.create_user(body = user)
            assert response.status_code == Responses.USER_WITHOUT_ONE_FIELD["status_code"]
            assert response.json()["success"] == Responses.USER_WITHOUT_ONE_FIELD["success"]
            assert response.json()["message"] == Responses.USER_WITHOUT_ONE_FIELD["message"]