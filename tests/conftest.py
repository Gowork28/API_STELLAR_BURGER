import random
import json

import allure
import pytest
import string

from data.test_data import TestUserData
from methods.user_methods import UserMethods


@pytest.fixture
def unique_user():
    with allure.step("Генератор рандомных данных"):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    with allure.step("Собираем тело запроса с рандомными данными"):
        body = {}

        body["email"] = f"{generate_random_string(10)}@random.com"
        body["password"] = generate_random_string(10)
        body["name"] = generate_random_string(10)

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
    with allure.step("Генератор рандомных данных"):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    with allure.step("Собираем тело запроса с рандомными данными"):
        body = {}

        body["email"] = f"{generate_random_string(10)}@random.com"
        body["password"] = generate_random_string(10)
        body["name"] = generate_random_string(10)

    with allure.step("Создаем пользователя и получаем токен из ответа"):
        UserMethods.create_user(body)
        token = UserMethods.login_user(body["email"], body["password"])
        access_token = token.json()["accessToken"]

        yield access_token

        UserMethods.delete_user(access_token)
