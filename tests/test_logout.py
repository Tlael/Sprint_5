from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD
from locators import FIELD_EMAIL, FIELD_PASSWORD, BUTTON_LOGIN, BUTTON_ACCOUNT, BUTTON_LOGOUT_IN_PROFILE
from urls import LOGIN_URL, PROFILE_URL


class TestLogout:

    def test_logout(self, browser, go_to_login_page):
        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Кликнуть по кнопке Личный кабинет
        browser.find_element(*BUTTON_ACCOUNT).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be(PROFILE_URL)
        )

        # Кликнуть по кнопке Выход
        browser.find_element(*BUTTON_LOGOUT_IN_PROFILE).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )

        # Проверить что url = LOGIN_URL
        assert browser.current_url == LOGIN_URL
