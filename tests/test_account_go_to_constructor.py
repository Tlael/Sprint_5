from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAccountToGoConstructor:
    def test_to_go_constructor(self, browser, go_to_main_page, send_email, send_pass):
        # Кликнуть по кнопке Войти в аккаунт
        browser.find_element(By.XPATH, '//section[2]/div/button').click()

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(send_email)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(send_pass)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Кликнуть по кнопке Личный кабинет
        browser.find_element(By.XPATH, '//header/nav/a').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile')
        )

        # Кликнуть по кнопке Конструктор
        browser.find_element(By.XPATH, '//li/a').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/')
        )

        # Проверить что url = https://stellarburgers.nomoreparties.site/
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
