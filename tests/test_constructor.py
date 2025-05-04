from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver


class TestConstructor:

    def test_go_to_sousy(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        assert driver.find_element(*Locators.proverka_sauces)


    def test_go_to_fillings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        assert driver.find_element(*Locators.proverka_fillings)

    def test_go_to_buns(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.buns_block).click()
        assert driver.find_element(*Locators.proverka_buns)
