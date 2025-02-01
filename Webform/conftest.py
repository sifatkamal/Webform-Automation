import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
    driver_path = r"C:/SeleniumDrivers"
    os.environ['PATH'] += os.pathsep + driver_path
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)
    driver.get("https://www.digitalunite.com/practice-webform-learners")
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.close()