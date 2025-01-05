from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import NAME, EMAIL, PASSWORD, INCORRECT_PASSWORD


class TestRegistration:

    def test_registration_correct_pass(self, browser, go_to_registration_page):
        # Заполнить поле Имя
        browser.find_element(By.XPATH, '//label[text()="Имя"]/../input').send_keys(NAME)

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(PASSWORD)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div')))

        # Найти текст и проверить, что он равен 'Войти'
        assert browser.find_element(By.XPATH, '//a[text()="Войти"]')

    # incorrect
    def test_registration_wrong_pass(self, browser, go_to_registration_page):
        # Заполнить поле Имя
        browser.find_element(By.XPATH, '//label[text()="Имя"]/../input').send_keys(NAME)

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(EMAIL)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(INCORRECT_PASSWORD)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()

        # Найти сообщение об ошибке и проверить, что текст равен 'Некорректный пароль'
        assert browser.find_element(By.XPATH, '//p[text()="Некорректный пароль"]')
