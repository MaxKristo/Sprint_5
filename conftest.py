import pytest
from selenium import webdriver
from data import Data
from Urls import Url

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()                       # создали объект для опций
    driver.set_window_size(1920, 1080)   # задали размер окна
    driver.get(Url.stellar_burgers_url)              # запуск страницы Stellar Burgers
    return driver
    driver.quit()