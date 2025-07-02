import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
