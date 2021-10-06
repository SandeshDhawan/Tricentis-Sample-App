import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class ProductDataPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def enter_start_date(self):
        start_date = datetime.datetime.today() + relativedelta(days=1)
        start_date = start_date + relativedelta(months=1)
        start_date = start_date.strftime("%m/%d/%Y")
        self.driver.find_element(By.ID, self.STARTDATE).send_keys(start_date)

    def select_insurance_sum(self, test_data):
        insurance_sum = test_data['vehicle_Insurance_details']['Product_Data']['Insurance_Sum']
        self.select_by_value(self.INSURANCE_SUM, insurance_sum)

    def select_merit_rating(self, test_data):
        merit_rating = test_data['vehicle_Insurance_details']['Product_Data']['Merit_Rating']
        self.select_by_value(self.MERIT_RATING, merit_rating)

    def select_courtesy_car(self, test_data):
        courtesy_car = test_data['vehicle_Insurance_details']['Product_Data']['Courtesy_Car']
        self.select_by_value(self.COURTESY_CAR, courtesy_car)

    def select_damage_insurance(self, test_data):
        damage_insurance = test_data['vehicle_Insurance_details']['Product_Data']['Damage_Infrastructure']
        self.select_by_value(self.DAMEGE_INSURANCE, damage_insurance)

    def select_optional_products(self, test_data):
        optional_products = test_data['vehicle_Insurance_details']['Product_Data']['Optional_Products']
        self.driver.find_element(By.XPATH, self.OPTIONAL_PRODUCTS.format(optional_products)).click()

    def click_next_button(self):
        self.driver.find_element(By.ID, self.NEXT_BUTTON).click()

    def enter_product_data(self, test_data):
        self.enter_start_date()
        self.select_insurance_sum(test_data)
        self.select_merit_rating(test_data)
        self.select_damage_insurance(test_data)
        self.select_optional_products(test_data)
        self.select_courtesy_car(test_data)
        self.click_next_button()

    STARTDATE = "startdate"
    INSURANCE_SUM = "//select[@id='insurancesum']"
    DAMEGE_INSURANCE = "//select[@id='damageinsurance']"
    OPTIONAL_PRODUCTS = "//label[@class='ideal-radiocheck-label']/input[@id='{}']//following-sibling::span"
    NEXT_BUTTON = "nextselectpriceoption"
    MERIT_RATING = "//select[@id='meritrating']"
    COURTESY_CAR = "//select[@id='courtesycar']"
