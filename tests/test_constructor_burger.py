from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorBurgers:
    def test_check_bun(self, browser, go_to_main_page):
        # Кликнуть на раздел Соусы
        browser.find_element(By.XPATH, "//span[text() = 'Соусы']").click()

        # Кликнуть на раздел Булки
        browser.find_element(By.XPATH, "//span[text() = 'Булки']").click()

        # Найти элемент и проверить его текст
        fillings = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Булки']/..")))
        fillings_text = fillings.text

        assert fillings_text == 'Булки'

    def test_check_fillings(self, browser, go_to_main_page):
        # Кликнуть на раздел Начинки
        browser.find_element(By.XPATH, "//span[text() = 'Начинки']").click()

        # Найти элемент и проверить его текст
        fillings = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']/..")))
        fillings_text = fillings.text

        assert fillings_text == 'Начинки'

    def test_check_sauces(self, browser, go_to_main_page):
        # Кликнуть на раздел Соусы
        browser.find_element(By.XPATH, "//span[text() = 'Соусы']").click()

        # Найти элемент и проверить его текст
        fillings = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']/..")))
        fillings_text = fillings.text

        assert fillings_text == 'Соусы'
