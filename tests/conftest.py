import json
import allure
import pytest

from helpers import generate_random_user_body

from data.test_data import TestUserData
from methods.user_methods import UserMethods


@pytest.fixture
def unique_user():
    with allure.step("Собираем тело запроса с рандомными данными"):
        body = generate_random_user_body()

        yield body

        token = UserMethods.login_user(body["email"], body["password"])
        access_token = token.json()["accessToken"]
        UserMethods.delete_user(access_token)


@pytest.fixture
def exist_user():
    with allure.step("Создаем существующего пользователя"):
        body = TestUserData.UserData.copy()
        UserMethods.create_user(body)

        yield body

        token = UserMethods.login_user(body["email"], body["password"])
        access_token = token.json()["accessToken"]
        UserMethods.delete_user(access_token)


@pytest.fixture
def auth_user():
    with allure.step("Собираем тело запроса с рандомными данными"):
        body = generate_random_user_body()

    with allure.step("Создаем пользователя и получаем токен из ответа"):
        UserMethods.create_user(body)
        token = UserMethods.login_user(body["email"], body["password"])
        access_token = token.json()["accessToken"]

        yield access_token

        UserMethods.delete_user(access_token)
