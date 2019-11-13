from time import sleep
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome('../chrome_driver_v78/chromedriver.exe')
    sleep(1)
    yield driver
    driver.quit()
