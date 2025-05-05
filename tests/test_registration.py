import pytest
from data import Data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver


class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями
    def test_registration_new_account_success_submit(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(Data.username)
        driver.find_element(*Locators.fields_email).send_keys(Data.random_email)
        driver.find_element(*Locators.fields_password).send_keys(Data.random_password)
        driver.find_element(*Locators.button_submit).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_title)).text == 'Вход'



    #Регистрация пользователя с некорректным паролем
    @pytest.mark.parametrize('invalid_password', ['12345', ' '])
    def test_login_with_incorrect_registration_error(self,driver,invalid_password):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(Data.username)
        driver.find_element(*Locators.fields_email).send_keys(Data.random_email)
        driver.find_element(*Locators.fields_password).send_keys(invalid_password)
        driver.find_element(*Locators.button_submit).click()
        assert driver.find_element(*Locators.incorrect_password).text == 'Некорректный пароль'
