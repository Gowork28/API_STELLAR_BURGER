import allure
import pytest

from data.test_data import Responses, TestIngredientData
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title("Код 200 при создании заказа авторизованным пользователем и с ингредиентами")
    def test_create_order_authorized_user_success(self, auth_user):
        with allure.step("Получаем токен авторизованного пользователя"):
            token = auth_user
        with allure.step("Передаем токен и игредиенты в запрос"):
            response = OrderMethods.create_order(token, body = TestIngredientData.IngredientData)
            assert response.status_code == Responses.OK_200["status_code"]
            assert response.json()["success"] == True


    @allure.title("Код 200 при создании заказа неавторизованным пользователем")
    def test_create_order_non_authorized_user_no_result(self, unique_user):
        with allure.step("Создаем уникального пользователя, но без авторизации"):
            UserMethods.create_user(body = unique_user)
        with allure.step("Пробуем сделать заказ"):
            response = OrderMethods.create_order(token = '', body = TestIngredientData.IngredientData)
            assert response.status_code == Responses.OK_200["status_code"]
            assert response.json()["success"] == True


    @allure.title("Код 400 при попытке создать заказ без ингредиентов")
    def test_create_order_without_ingredients_fail(self, auth_user):
        with allure.step("Получаем токен авторизованного пользователя"):
            token = auth_user
        with allure.step("Передаем токен и игредиенты в запрос"):
            response = OrderMethods.create_order(token, body = None)
            assert response.status_code == Responses.ORDER_WITHOUT_INGREDIENTS["status_code"]
            assert response.json()["success"] == Responses.ORDER_WITHOUT_INGREDIENTS["success"]
            assert response.json()["message"] == Responses.ORDER_WITHOUT_INGREDIENTS["message"]


    @allure.title("Код 500 при попытке создать заказ с неверным хешем ингредиентов")
    def test_create_order_wrong_hash_ingredients_fail(self, auth_user):
        with allure.step("Получаем токен авторизованного пользователя"):
            token = auth_user
        with allure.step("Передаем токен и игредиенты в запрос"):
            wrong_hash = {
                "ingredients": ["111a11n111y111a"]
            }
            response = OrderMethods.create_order(token, body=wrong_hash)
            assert response.status_code == Responses.ORDER_WITH_WRONG_INGREDIENT_HASH["status_code"]