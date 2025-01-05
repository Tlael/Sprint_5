from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD
from locators import LINK_LOGIN, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_LOGIN, BUTTON_LOGIN_IN_ACCOUNT, BUTTON_ACCOUNT


class TestLogin:
    def test_registration_login(self, browser, go_to_registration_page):
        # Кликнуть по ссылке Войти
        browser.find_element(*LINK_LOGIN).click()

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(BUTTON_LOGIN_IN_ACCOUNT))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).text == 'Оформить заказ'

    def test_forgot_pass_login(self, browser, go_to_forgot_page):
        # Кликнуть по ссылке Войти
        browser.find_element(*LINK_LOGIN).click()

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(BUTTON_LOGIN_IN_ACCOUNT))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).text == 'Оформить заказ'

    def test_main_page_login(self, browser, go_to_main_page):
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

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).text == 'Оформить заказ'

    def test_profile_login(self, browser, go_to_main_page):
        # Кликнуть по кнопке Личный кабинет
        browser.find_element(*BUTTON_ACCOUNT).click()

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(*BUTTON_LOGIN).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(BUTTON_LOGIN_IN_ACCOUNT))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(*BUTTON_LOGIN_IN_ACCOUNT).text == 'Оформить заказ'
