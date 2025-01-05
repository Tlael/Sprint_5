from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD
from locators import BUTTON_ACCOUNT, BUTTON_LOGIN, FIELD_PASSWORD, FIELD_EMAIL, BUTTON_LOGIN_IN_ACCOUNT


class TestGoAccount:
    def test_registration_login(self, browser, go_to_main_page):
        # Кликнуть по кнопке Войти в аккаунт
        browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).click()

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(BUTTON_LOGIN_IN_ACCOUNT))

        # Кликнуть по кнопке Личный кабинет
        browser.find_element(*BUTTON_ACCOUNT).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile')
        )

        # Проверить что url = https://stellarburgers.nomoreparties.site/account/profile
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
