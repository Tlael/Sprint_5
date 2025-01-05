from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import SECTION_SAUCES, SECTION_BUNS, SECTION_FILLINGS


class TestConstructorBurgers:
    def test_check_bun(self, browser, go_to_main_page):
        # Кликнуть на раздел Соусы
        browser.find_element(*SECTION_SAUCES).click()

        # Кликнуть на раздел Булки
        browser.find_element(*SECTION_BUNS).click()

        # Найти элемент и проверить его текст
        buns = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(SECTION_BUNS))
        buns_text = buns.text

        assert buns_text == 'Булки'

    def test_check_fillings(self, browser, go_to_main_page):
        # Кликнуть на раздел Начинки
        browser.find_element(*SECTION_FILLINGS).click()

        # Найти элемент и проверить его текст
        fillings = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(SECTION_FILLINGS))
        fillings_text = fillings.text

        assert fillings_text == 'Начинки'

    def test_check_sauces(self, browser, go_to_main_page):
        # Кликнуть на раздел Соусы
        browser.find_element(*SECTION_SAUCES).click()

        # Найти элемент и проверить его текст
        sauces = WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(SECTION_SAUCES))
        sauces_text = sauces.text

        assert sauces_text == 'Соусы'
