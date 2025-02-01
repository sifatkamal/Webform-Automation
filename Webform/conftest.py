import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="class")
def setup():

    driver_path = r"C:/SeleniumDrivers"
    os.environ['PATH'] += driver_path
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)
    driver.maximize_window()