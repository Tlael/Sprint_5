from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD
from locators import BUTTON_LOGIN_IN_ACCOUNT, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_LOGIN, BUTTON_ACCOUNT, \
    BUTTON_CONSTRUCTOR
from urls import MAIN_PAGE


class TestAccountToGoConstructor:
    def test_to_go_constructor(self, browser, go_to_main_page):
        # Кликнуть по кнопке Войти в аккаунт
        browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).click()

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Кликнуть по кнопке Личный кабинет
        browser.find_element(*BUTTON_ACCOUNT).click()

        # Кликнуть по кнопке Конструктор
        browser.find_element(*BUTTON_CONSTRUCTOR).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be(MAIN_PAGE)
        )

        # Проверить что url = MAIN_PAGE
        assert browser.current_url == MAIN_PAGE
