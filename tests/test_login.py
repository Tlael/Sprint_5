from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD


class TestLogin:
    def test_registration_login(self, browser, go_to_registration_page):
        # Кликнуть по ссылке Войти
        browser.find_element(By.LINK_TEXT, 'Войти').click()

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(By.XPATH, '//section[2]/div/button').text == 'Оформить заказ'

    def test_forgot_pass_login(self, browser, go_to_forgot_page):
        # Кликнуть по ссылке Войти
        browser.find_element(By.LINK_TEXT, 'Войти').click()

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(By.XPATH, '//section[2]/div/button').text == 'Оформить заказ'

    def test_main_page_login(self, browser, go_to_main_page):
        # Кликнуть по кнопке Войти в аккаунт
        browser.find_element(By.XPATH, '//section[2]/div/button').click()

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(By.XPATH, '//section[2]/div/button').text == 'Оформить заказ'

    def test_profile_login(self, browser, go_to_main_page):
        # Кликнуть по кнопке Личный кабинет
        browser.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Войти
        browser.find_element(By.XPATH, '//form/button').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//section[2]/div/button')))

        # Найти кнопку, получить её текст и проверить, что он равен 'Выйти'
        assert browser.find_element(By.XPATH, '//section[2]/div/button').text == 'Оформить заказ'
