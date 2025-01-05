from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD


class TestLogout:

    def test_logout(self, browser, go_to_login_page):
        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Кликнуть по кнопке Личный кабинет
        browser.find_element(By.XPATH, "//p[text()='Личный Кабинет']/..").click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile')
        )

        # Кликнуть по кнопке Выход
        browser.find_element(By.XPATH, "//button[text()='Выход']").click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login')
        )

        # Проверить что url = https://stellarburgers.nomoreparties.site/login
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'
