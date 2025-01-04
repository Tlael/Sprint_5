import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
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


@pytest.fixture
def send_name(browser):
    """Фикстура для отправки email"""
    name = "Виктория"
    yield name


@pytest.fixture
def send_email(browser):
    """Фикстура для отправки email"""
    email = "Vika_Pavlova_17@yandex.ru"
    yield email


@pytest.fixture
def send_pass(browser):
    """Фикстура для отправки пароля"""
    password = "123456"
    yield password


@pytest.fixture
def send_incorrect_pass(browser):
    """Фикстура для отправки некорректного пароля"""
    password = "1234"
    yield password
