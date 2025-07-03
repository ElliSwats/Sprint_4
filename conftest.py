import pytest
from selenium import webdriver

from data import main_page_url


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    url = main_page_url
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
