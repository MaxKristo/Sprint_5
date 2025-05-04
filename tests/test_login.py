from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
from conftest import driver

class Testlogin:


    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_login_to_account_on_home(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'
        # не совсем понимаю про какие тестовые данные имеются ввиду (email and password вынесены в data)


    def test_enter_button_personal_account(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'


    def test_enter_button_in_the_registration_form(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_in_registration_form))
        driver.find_element(*Locators.button_login_in_registration_form).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'


    def test_button_in_the_password_recovery_form(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_forgot_password))
        driver.find_element(*Locators.button_forgot_password).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_passwd_recovery_form))
        driver.find_element(*Locators.button_login_passwd_recovery_form).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(Data.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(Data.password)
        driver.find_element(*Locators.button_login).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order)).text == 'Оформить заказ'

