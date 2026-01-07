import requests
import allure
from data.urls import UrlsForTest

class OrderMethods:

    @staticmethod
    @allure.title("Создание заказа")
    def create_order(token, body):
        header = {"Authorization":token}
        return requests.post(url=UrlsForTest.CREATE_ORDER_URL, headers=header, json=body)