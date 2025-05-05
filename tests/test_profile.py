from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
from conftest import driver

class Test_profile:

    def test_click_profile(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile)).text == 'Профиль'


    def test_click_through_to_the_Constructor(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.header_of_page_constructor).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'


    def test_click_on_the_Stellar_Burgers_logo(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo_Stellar_Burgers).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'


    def test_log_out_of_your_account(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_logout))
        driver.find_element(*Locators.button_logout).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_title)).text == 'Вход'


