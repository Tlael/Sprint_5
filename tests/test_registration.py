from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_correct_pass(self, browser, go_to_registration_page, send_name, send_email, send_pass):
        # Заполнить поле Имя
        browser.find_element(By.XPATH, '//label[text()="Имя"]/../input').send_keys(send_name)

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(send_email)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(send_pass)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()

        # Явное ожидание загрузки страницы
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div')))

        # Найти текст и проверить, что он равен 'Войти'
        assert browser.find_element(By.XPATH, '//a[text()="Войти"]')

    # incorrect
    def test_registration_wrong_pass(self, browser, go_to_registration_page, send_name, send_email,
                                     send_incorrect_pass):
        # Заполнить поле Имя
        browser.find_element(By.XPATH, '//label[text()="Имя"]/../input').send_keys(send_name)

        # Заполнить поле Email
        browser.find_element(By.XPATH, '//label[text()="Email"]/../input').send_keys(send_email)

        # Заполнить поле Пароль
        browser.find_element(By.XPATH, '//label[text()="Пароль"]/../input').send_keys(send_incorrect_pass)

        # Кликнуть по кнопке Зарегистрироваться
        browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()

        # Найти сообщение об ошибке и проверить, что текст равен 'Некорректный пароль'
        assert browser.find_element(By.XPATH, '//p[text()="Некорректный пароль"]')
