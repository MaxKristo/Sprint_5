from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver


class TestConstructor:

    # проверка работы перехода к разделу "Булки"
    def test_go_to_buns(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.buns_block).click()
        #element_buns = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        #assert element_buns.is_displayed()
        current_element_is_visible = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.current_section))
        assert current_element_is_visible

    # проверка работы перехода к разделу "Соусы"
    def test_go_to_sousy(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        #element_sousy = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        #assert element_sousy.is_displayed()
        current_element_is_visible = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.current_section))
        assert current_element_is_visible

    # проверка работы перехода к разделу "Начинки"
    def test_go_to_fillings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        #element_fillings= WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        #assert element_fillings.is_displayed()
        current_element_is_visible = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.current_section))
        assert current_element_is_visible