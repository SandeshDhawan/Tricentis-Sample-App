import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_present(self, time, locator, locator_type):
        if locator_type == "ID":
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, locator)))

        elif locator_type == "XPATH":
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, locator)))

    def wait_until_element_is_displayed(self, time, locator):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def implicit_wait(self, time):
        self.driver.implicitly_wait(time)

    def get_test_data(self, file_name):
        test_data_file_path = os.getcwd().replace("tests", "test_data") + "\\" + file_name
        with open(test_data_file_path) as f:
            payload = json.load(f)
        return payload

    def select_by_value(self, locator, value):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_value(value)

