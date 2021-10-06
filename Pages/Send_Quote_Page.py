import time

from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class SendQuotePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def enter_email(self, test_data):
        email = test_data['vehicle_Insurance_details']['Send_Quote']['Email']
        self.driver.find_element(By.ID, self.EMAIL).send_keys(email)

    def enter_phone(self, test_data):
        phone = test_data['vehicle_Insurance_details']['Send_Quote']['Phone']
        self.driver.find_element(By.ID, self.PHONE).send_keys(phone)

    def enter_username(self, test_data):
        username = test_data['vehicle_Insurance_details']['Send_Quote']['UserName']
        self.driver.find_element(By.ID, self.USERNAME).send_keys(username)

    def enter_password(self, test_data):
        password = test_data['vehicle_Insurance_details']['Send_Quote']['Password']
        self.driver.find_element(By.ID, self.PASSWORD).send_keys(password)

    def enter_confirm_password(self, test_data):
        password = test_data['vehicle_Insurance_details']['Send_Quote']['Password']
        self.driver.find_element(By.ID, self.CONFIRM_PASSWORD).send_keys(password)

    def enter_comments(self, test_data):
        comments = test_data['vehicle_Insurance_details']['Send_Quote']['Comments']
        self.driver.find_element(By.ID, self.COMMENTS).send_keys(comments)

    def send_quote(self):
        self.driver.find_element(By.ID, self.SEND).click()

    def enter_send_quote_details(self, test_data):
        self.enter_email(test_data)
        self.enter_phone(test_data)
        self.enter_username(test_data)
        self.enter_password(test_data)
        self.enter_confirm_password(test_data)
        self.enter_comments(test_data)
        self.send_quote()

    EMAIL = "email"
    PHONE = "phone"
    USERNAME = "username"
    PASSWORD = "password"
    CONFIRM_PASSWORD = "confirmpassword"
    COMMENTS = "Comments"
    SEND = "sendemail"
