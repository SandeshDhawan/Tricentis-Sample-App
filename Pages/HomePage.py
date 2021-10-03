from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def verify_tricentis_logo(self):
        status = self.driver.find_element(By.ID, self.TRICENTIS_LOGO).is_displayed()
        assert status == True, "Tricentis Logo is Not Present"

    def verify_request_demo_button(self):
        status = self.driver.find_element(By.ID, self.REQUEST_DEMO).is_enabled()
        assert status == True, "Request Demo is Disabled"

    def verify_visit_support_button(self):
        status = self.driver.find_element(By.ID, self.VISIT_SUPPORT).is_enabled()
        assert status == True, "Visit Support Button is Disabled"

    def verify_vehicle_header_links(self):
        self.verify_automobile_header_link()
        self.verify_truck_header_link()
        self.verify_motorcycle_header_link()
        self.verify_camper_header_link()

    def verify_automobile_header_link(self):
        status = self.driver.find_element(By.ID, self.AUTOMOBILE_HEADER).is_enabled()
        assert status == True, "Automobile Button is Disabled"

    def verify_truck_header_link(self):
        status = self.driver.find_element(By.ID, self.TRUCK_HEADER).is_enabled()
        assert status == True, "Truck Button is Disabled"

    def verify_motorcycle_header_link(self):
        status = self.driver.find_element(By.ID, self.MOTORCYCLE_HEADER).is_enabled()
        assert status == True, "Motorcycle Button is Disabled"

    def verify_camper_header_link(self):
        status = self.driver.find_element(By.ID, self.CAMPER_HEADER).is_enabled()
        assert status == True, "Camper Button is Disabled"

    def verify_get_a_quote_link(self):
        status = self.driver.find_element(By.ID, self.GET_A_QUOTE).is_enabled()
        assert status == True, "Get a quote button is disabled"

    def verify_automobile_page_link(self):
        status = self.driver.find_element(By.XPATH, self.AUTOMOBILE_PAGE).is_enabled()
        assert status == True, "Automobile Button is Disabled"

    def verify_truck_page_link(self):
        status = self.driver.find_element(By.XPATH, self.TRUCK_PAGE).is_enabled()
        assert status == True, "Truck Button is Disabled"

    def verify_motorcycle_page_link(self):
        status = self.driver.find_element(By.XPATH, self.MOTORCYCLE_PAGE).is_enabled()
        assert status == True, "Motorcycle Button is Disabled"

    def verify_camper_page_link(self):
        status = self.driver.find_element(By.XPATH, self.CAMPER_PAGE).is_enabled()
        assert status == True, "Camper Button is Disabled"

    def verify_vehicle_page_links(self):
        self.verify_automobile_page_link()
        self.verify_truck_page_link()
        self.verify_motorcycle_page_link()
        self.verify_camper_page_link()

    def click_automobile_header_link(self):
        self.driver.find_element(By.ID, self.AUTOMOBILE_HEADER).click()

    def click_truck_header_link(self):
        self.driver.find_element(By.ID, self.TRUCK_HEADER).click()

    def click_motorcycle_header_link(self):
        self.driver.find_element(By.ID, self.MOTORCYCLE_HEADER).click()

    def click_camper_header_link(self):
        self.driver.find_element(By.ID, self.CAMPER_HEADER).click()

    def click_automobile_page_link(self):
        self.driver.find_element(By.XPATH, self.AUTOMOBILE_PAGE).click()

    def click_truck_page_link(self):
        self.driver.find_element(By.XPATH, self.TRUCK_PAGE).click()

    def click_motorcycle_page_link(self):
        self.driver.find_element(By.XPATH, self.MOTORCYCLE_PAGE).click()

    def click_camper_page_link(self):
        self.driver.find_element(By.XPATH, self.CAMPER_PAGE).click()

    def verify_selected_insurance(self):
        return self.driver.find_element(By.ID, self.SELECTEDINSURANCE).text

    def navigate_to_request_demo(self):
        self.driver.find_element(By.ID, self.REQUEST_DEMO)

    TRICENTIS_LOGO = "tricentis_logo"
    REQUEST_DEMO = "downloadtrial"
    VISIT_SUPPORT = "visitsupport"
    AUTOMOBILE_HEADER = "nav_automobile"
    TRUCK_HEADER = "nav_truck"
    MOTORCYCLE_HEADER = "nav_motorcycle"
    CAMPER_HEADER = "nav_camper"
    GET_A_QUOTE = "get_automobile"
    AUTOMOBILE_PAGE = "//a[@id='offer_automobile']/img"
    TRUCK_PAGE = "//a[@id='offer_truck']/img"
    MOTORCYCLE_PAGE = "//a[@id='offer_motorcycle']/img"
    CAMPER_PAGE = "//a[@id='offer_camper']/img"
    SELECTEDINSURANCE = "selectedinsurance"
