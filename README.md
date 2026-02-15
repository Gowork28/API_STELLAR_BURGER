# Тестирование API для сервиса Stellar Burger

Stellar Burger - это космический сервис онлайн - заказа бургера. 
Можно выбрать булку, начинку и соус. После оформления заказа пользователь получает номер заказа. 

В этом проекте реализованы автоматизированные тесты для функций API сервиса Stellar Burger. Проведены как позитивные, так и негативные проверки. Проверки проходили с помощью сравнения кода и статуса ответа, тела ответа.

## Проверенные функции

- **Создание уникального пользователя** - проверка возможности создания уникального пользователя.  
- **Логин пользователя** - проверка авторизации пользователя по email и password.
- **Создание заказа** – проверка возможности создания нового заказа. 

## Стек:
<div align="left">
  <img src="https://img.shields.io/badge/ApiDoc-009688?style=for-the-badge&logo=readthedocs&logoColor=white" alt="ApiDoc"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman"/>
  <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white" alt="PyCharm"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium"/>
  <img src="https://img.shields.io/badge/Allure-FF8C00?style=for-the-badge&logo=allure&logoColor=white" alt="Allure"/>
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON"/>
</div>

## Инструкция по запуску:

1. Установите зависимости:
pip install -r requirements.txt

2. Запустить все тесты и записать отчет:
pytest tests --alluredir=allure_results

3. Посмотреть отчет по прогону html
allure serve allure_results
