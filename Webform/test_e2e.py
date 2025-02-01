import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
from utilities.BaseClass import BaseClass

class TestWebform(BaseClass):

    def test_e2e(self):

        time.sleep(5)

        cookie = self.driver.find_elements(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']")

        if cookie != []:

            self.driver.find_element(By.CSS_SELECTOR, "button[class='onetrust-close-btn-handler ot-close-icon banner-close-button']").click()

        self.driver.find_element(By.CSS_SELECTOR, "input[data-drupal-selector='edit-name']").send_keys("Dexter")

        self.driver.find_element(By.CSS_SELECTOR, "[data-drupal-selector='edit-number']").send_keys("(555) 123-4567")

        calender_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")

        calender_input.click()

        self.driver.find_element(By.CSS_SELECTOR, 'input[data-drupal-selector="edit-email"]').send_keys("xyz@gmail.com")

        self.driver.find_element(By.CSS_SELECTOR, '[data-drupal-selector="edit-tell-us-a-bit-about-yourself-"]').send_keys("Hi, my name is Alex. I am a detail-oriented and curious person who enjoys solving problems and learning new things. In my free time, I like reading, exploring new technologies, and working on small coding projects. I enjoy collaborating with others and always look for ways to improve my skills. I believe in staying positive and embracing challenges as opportunities to grow.")

        self.driver.find_element(By.CSS_SELECTOR, '[data-drupal-selector="edit-age"]').click()

