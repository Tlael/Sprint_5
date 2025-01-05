from data import NAME, EMAIL, PASSWORD, INCORRECT_PASSWORD
from locators import FIELD_NAME, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_REGISTER, MESSAGE_INCORRECT_PASS, \
    MESSAGE_AFTER_REGISTER


class TestRegistration:

    def test_registration_correct_pass(self, browser, go_to_registration_page):
        # Заполнить поле Имя
        browser.find_element(*FIELD_NAME).send_keys(NAME)

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(PASSWORD)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(*BUTTON_REGISTER).click()

        # Найти текст и проверить, что он равен 'Войти'
        message_after_register = browser.find_element(*MESSAGE_AFTER_REGISTER)
        assert message_after_register.text == 'Войти'

    # incorrect
    def test_registration_wrong_pass(self, browser, go_to_registration_page):
        # Заполнить поле Имя
        browser.find_element(*FIELD_NAME).send_keys(NAME)

        # Заполнить поле Email
        browser.find_element(*FIELD_EMAIL).send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(*FIELD_PASSWORD).send_keys(INCORRECT_PASSWORD)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(*BUTTON_REGISTER).click()

        # Найти сообщение об ошибке и проверить, что текст равен 'Некорректный пароль'
        assert browser.find_element(*MESSAGE_INCORRECT_PASS)
