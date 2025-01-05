import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    """Фикстура для запуска и закрытия браузера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def go_to_main_page(browser):
    """Фикстура для перехода на главную страницу"""
    browser.get("https://stellarburgers.nomoreparties.site")


@pytest.fixture()
def go_to_registration_page(browser):
    """Фикстура для перехода на страницу регистрации"""
    browser.get("https://stellarburgers.nomoreparties.site/register")


@pytest.fixture()
def go_to_login_page(browser):
    """Фикстура для перехода на страницу логина"""
    browser.get("https://stellarburgers.nomoreparties.site/login")


@pytest.fixture()
def go_to_forgot_page(browser):
    """Фикстура для перехода на страницу восстановления пароля"""
    browser.get("https://stellarburgers.nomoreparties.site/forgot-password")

