import requests
import allure
from data.urls import UrlsForTest

class UserMethods:

    @staticmethod
    @allure.title('Создание пользователя')
    def create_user(body):
        return requests.post(url=UrlsForTest.CREATE_USER_URL, json=body)

    @staticmethod
    @allure.title('Логин пользователя')
    def login_user(email, password):
        body = {
            "email": email,
            "password": password
        }
        return requests.post(url=UrlsForTest.AUTH_USER_URL, json=body)

    @staticmethod
    @allure.title('Удаление пользователя')
    def delete_user(token):
        header = {"Authorization": token}
        return requests.delete(url=UrlsForTest.DELETE_USER_URL, headers=header)
