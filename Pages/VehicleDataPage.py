from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class VehicleDataPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def enter_vehicle_data(self, test_data):
        self.select_make(test_data)
        self.enter_engine_performance(test_data)
        self.enter_date_of_manufacture(test_data)
        self.select_number_of_seats(test_data)
        self.select_fuel_type(test_data)
        self.enter_list_price(test_data)
        self.enter_licenece_plate_number(test_data)
        self.enter_annual_mileage(test_data)
        self.click_next_button()

    def select_make(self, test_data):
        make = test_data['vehicle_Insurance_details']['vehicle_data']['Make']
        self.select_by_value(self.MAKE_DROPDOWN, make)

    def enter_engine_performance(self, test_data):
        engine_performance = test_data['vehicle_Insurance_details']['vehicle_data']['Engine_Performance']
        self.wait_until_element_is_present(20, self.ENGINE_PERFORMANCE, "XPATH")
        self.driver.find_element(By.XPATH, self.ENGINE_PERFORMANCE).clear()
        self.driver.find_element(By.XPATH, self.ENGINE_PERFORMANCE).send_keys(engine_performance)

    def enter_date_of_manufacture(self, test_data):
        date_of_manufacture = test_data['vehicle_Insurance_details']['vehicle_data']['Date_Of_Manufacture']
        self.driver.find_element(By.XPATH, self.DATE_OF_MANUFACTURE).send_keys(date_of_manufacture)

    def select_number_of_seats(self, test_data):
        number_of_seats = test_data['vehicle_Insurance_details']['vehicle_data']['Number_Of_Seats']
        self.select_by_value(self.NUMBER_OF_SEATS, number_of_seats)

    def select_fuel_type(self, test_data):
        fuel_type = test_data['vehicle_Insurance_details']['vehicle_data']['Fuel_Type']
        self.select_by_value(self.FUEL_TYPE, fuel_type)

    def enter_list_price(self, test_data):
        price = test_data['vehicle_Insurance_details']['vehicle_data']['List_Price']
        self.wait_until_element_is_present(10, self.LIST_PRICE, "XPATH")
        self.driver.find_element(By.XPATH, self.LIST_PRICE).clear()
        self.driver.find_element(By.XPATH, self.LIST_PRICE).send_keys(price)

    def enter_licenece_plate_number(self, test_data):
        license_plate_number = test_data['vehicle_Insurance_details']['vehicle_data']['Licence_Plate_Number']
        self.driver.find_element(By.XPATH, self.LICENCE_PLATE_NUMBER).send_keys(license_plate_number)

    def enter_annual_mileage(self, test_data):
        price = test_data['vehicle_Insurance_details']['vehicle_data']['Annual_Mileage']
        self.wait_until_element_is_present(10, self.ANNUAL_MILEAGE, "XPATH")
        self.driver.find_element(By.XPATH, self.ANNUAL_MILEAGE).clear()
        self.driver.find_element(By.XPATH, self.ANNUAL_MILEAGE).send_keys(price)

    def get_engine_performance_error_message(self):
        return self.driver.find_element(By.XPATH, self.ENGINE_PERFORMANCE_ERROR).text

    def get_list_price_error_message(self):
        return self.driver.find_element(By.XPATH, self.LIST_PRICE_ERROR).text

    def get_annual_mileage_error_message(self):
        return self.driver.find_element(By.XPATH, self.ANNUAL_MILEAGE_ERROR).text

    def click_next_button(self):
        self.driver.find_element(By.ID, self.NEXT_BUTTON).click()

    ENGINE_PERFORMANCE = "//input[@id='engineperformance']"
    ENGINE_PERFORMANCE_ERROR = "//span[@class='error']"
    LIST_PRICE = "//input[@id='listprice']"
    LIST_PRICE_ERROR = "//input[@id='listprice']/following-sibling::span"
    ANNUAL_MILEAGE = "//input[@id='annualmileage']"
    ANNUAL_MILEAGE_ERROR = "//input[@id='annualmileage']/following-sibling::span"
    NEXT_BUTTON = "nextenterinsurantdata"
    MAKE_DROPDOWN = "//select[@id='make']"
    DATE_OF_MANUFACTURE = "//input[@id='dateofmanufacture']"
    NUMBER_OF_SEATS = "//select[@id='numberofseats']"
    FUEL_TYPE = "//select[@id='fuel']"
    LICENCE_PLATE_NUMBER = "//input[@id='licenseplatenumber']"
