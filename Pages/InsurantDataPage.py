from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class InsurantDataPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def enter_first_name(self, test_data):
        first_name = test_data['vehicle_Insurance_details']['Insurance_Data']['First_Name']
        self.wait_until_element_is_present(20, self.FIRSTNAME, "ID")
        self.driver.find_element(By.ID, self.FIRSTNAME).clear()
        self.driver.find_element(By.ID, self.FIRSTNAME).send_keys(first_name)

    def enter_last_name(self, test_data):
        last_name = test_data['vehicle_Insurance_details']['Insurance_Data']['Last_Name']
        self.wait_until_element_is_present(20, self.LASTNAME, "ID")
        self.driver.find_element(By.ID, self.LASTNAME).clear()
        self.driver.find_element(By.ID, self.LASTNAME).send_keys(last_name)

    def enter_street_address(self, test_data):
        last_name = test_data['vehicle_Insurance_details']['Insurance_Data']['Street_Address']
        self.wait_until_element_is_present(20, self.STREET_ADDRESS, "ID")
        self.driver.find_element(By.ID, self.STREET_ADDRESS).clear()
        self.driver.find_element(By.ID, self.STREET_ADDRESS).send_keys(last_name)

    def enter_date_of_birth(self, test_data):
        last_name = test_data['vehicle_Insurance_details']['Insurance_Data']['Date_Of_Birth']
        self.wait_until_element_is_present(20, self.DATE_OF_BIRTH, "ID")
        self.driver.find_element(By.ID, self.DATE_OF_BIRTH).clear()
        self.driver.find_element(By.ID, self.DATE_OF_BIRTH).send_keys(last_name)

    def enter_zip_code(self, test_data):
        last_name = test_data['vehicle_Insurance_details']['Insurance_Data']['Zip_Code']
        self.wait_until_element_is_present(20, self.ZIP_CODE, "ID")
        self.driver.find_element(By.ID, self.ZIP_CODE).clear()
        self.driver.find_element(By.ID, self.ZIP_CODE).send_keys(last_name)

    def enter_website(self, test_data):
        last_name = test_data['vehicle_Insurance_details']['Insurance_Data']['Website']
        self.wait_until_element_is_present(20, self.WEBSITE, "ID")
        self.driver.find_element(By.ID, self.WEBSITE).clear()
        self.driver.find_element(By.ID, self.WEBSITE).send_keys(last_name)

    def get_first_name_error_message(self):
        return self.driver.find_element(By.XPATH, self.FIRSTNAME_ERROR).text

    def get_last_name_error_message(self):
        return self.driver.find_element(By.XPATH, self.LASTNAME_ERROR).text

    def get_street_address_error_message(self):
        return self.driver.find_element(By.XPATH, self.STREET_ADDRESS_ERROR).text

    def get_date_of_birth_error_message(self):
        return self.driver.find_element(By.XPATH, self.DATE_OF_BIRTH_ERROR).text

    def get_zip_code_error_message(self):
        return self.driver.find_element(By.XPATH, self.ZIP_CODE_ERROR).text

    def get_website_error_message(self):
        return self.driver.find_element(By.XPATH, self.WEBSITE_ERROR).text

    FIRSTNAME = "firstname"
    LASTNAME = "lastname"
    STREET_ADDRESS = "streetaddress"
    DATE_OF_BIRTH = "birthdate"
    ZIP_CODE = "zipcode"
    WEBSITE = "website"
    FIRSTNAME_ERROR = "//input[@id='firstname']/following-sibling::span"
    LASTNAME_ERROR = "//input[@id='lastname']/following-sibling::span"
    STREET_ADDRESS_ERROR = "//input[@id='streetaddress']/following-sibling::span"
    DATE_OF_BIRTH_ERROR = "//input[@id='birthdate']/following-sibling::span"
    ZIP_CODE_ERROR = "//input[@id='zipcode']/following-sibling::span"
    WEBSITE_ERROR = "//input[@id='website']/following-sibling::span"
