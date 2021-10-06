from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class PriceOptionPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def select_price_option(self, test_data):
        price_option = test_data['vehicle_Insurance_details']['Price_Option']['price_option']
        self.driver.find_element(By.XPATH, self.price_option_value.format(price_option)).click()

    def click_next_button(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.NEXT_BUTTON).click()


    price_option_value = "//input[@value = '{}']//following-sibling::span"
    NEXT_BUTTON = "nextsendquote"