import allure
import pytest

from data.test_data import Responses
from methods.user_methods import UserMethods


class TestLoginUser:

    @allure.title("Код 200 при успешном логине под существующим пользователем")
    def test_login_existing_user_success(self, unique_user):
        with allure.step("Создадим уникального пользователя"):
            UserMethods.create_user(unique_user)
        with allure.step("Авторизуемся под существующим пользователем"):
            response = UserMethods.login_user(unique_user["email"], unique_user["password"])
            assert response.status_code == Responses.OK_200["status_code"]
            assert response.json()["success"] == True
            assert "accessToken" in response.json()


    @pytest.mark.parametrize("key,value", [
        ("email", "pepepe@shepe.com"),
        ("password", "fafapepe"),
    ])
    @allure.description("Код 401 при попытке логина с неверным логином и паролем")
    def test_login_wrong_user_data_fail(self,unique_user, key, value):
        with allure.step("Создадим уникального пользователя"):
            UserMethods.create_user(unique_user)
        with allure.step(f"Авторизовываем пользователя с некорректными данными в поле {key}"):
            user = unique_user.copy()  # Работаем с копией данных, чтобы не нарушить логику teardown в фикстуре
            user[key] = value
            response = UserMethods.login_user(user["email"], user["password"])
            assert response.status_code == Responses.LOGIN_WITH_WRONG_DATA["status_code"]
            assert response.json()["success"] == Responses.LOGIN_WITH_WRONG_DATA["success"]
            assert response.json()["message"] == Responses.LOGIN_WITH_WRONG_DATA["message"]
