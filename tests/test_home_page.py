import time

import pytest
from Pages.HomePage import HomePage
#py.test -v -s --browser_name chrome --screenshot=on --screenshot_path=off --alluredir="C:\Users\Dhawan\PycharmProjects\TricentisSampleApp\reports"
# allure serve C:\Users\Dhawan\PycharmProjects\TricentisSampleApp\reports



@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_home_Page_details(self):
        """
        Given:
            Land on Tricentis website

        When:
            1. Verify Tricentis Logo
            2. Verify Request Demo Button
            3. Verify Visit Support Button
            4. Verify Automobile,Truck, Motorcycle,Camper Button present in header
            5. Verify Automobile,Truck, Motorcycle,Camper Button present in Page
            6. Verify "Get a Quote" Button

        Then:
            1. Trcientis Logo should be present
            2. Request Demo Button Should be present
            3. Visit Support Button Should be present
            4. Automobile,Truck,Motorcycle,Camper Button Should be present in header
            5. Automobile,Truck,Motorcycle,Camper Button Should be present in Page
            6. Get a Quote Button Should be present
        """
        homepage = HomePage(self.driver)
        homepage.verify_tricentis_logo()
        homepage.verify_request_demo_button()
        homepage.verify_visit_support_button()
        homepage.verify_vehicle_header_links()
        homepage.verify_get_a_quote_link()
        homepage.verify_vehicle_page_links()

    def test_verify_user_is_able_to_navigate_to_automobile_insurance_page_through_header(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Automobile Link present on header

                Then:
                    1. Automobile Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)

        homepage.click_automobile_header_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Automobile Insurance", "Automobile vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_truck_insurance_page_through_header(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Truck Link present on header

                Then:
                    1. Truck Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_truck_header_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Truck Insurance", "Truck vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_motorcycle_insurance_page_through_header(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Motorcycle Link present on header

                Then:
                    1. Motorcycle Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_motorcycle_header_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Motorcycle Insurance", "Motorcycle vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_camper_insurance_page_through_header(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Camper Link present on header

                Then:
                    1. Motorcycle Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_camper_header_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Camper Insurance", "Camper vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_automobile_insurance_page_through_page_link(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Automobile Link present on Page

                Then:
                    1. Automobile Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_automobile_page_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Automobile Insurance", "Automobile vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_truck_insurance_page_through_page_link(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Truck Link present on Page

                Then:
                    1. Truck Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_truck_page_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Truck Insurance", "Truck vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_motorcycle_insurance_page_through_page_link(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Motorcycle Link present on Page

                Then:
                    1. Motorcycle Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_motorcycle_page_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Motorcycle Insurance", "Motorcycle vehicle is not present"

    def test_verify_user_is_able_to_navigate_to_camper_insurance_page_through_page_link(self):
        """
                Given:
                    Land on Tricentis website

                When:
                    1. Click on Camper Link present on Page

                Then:
                    1. Motorcycle Insurance Page should be displayed
                """
        homepage = HomePage(self.driver)
        homepage.click_camper_page_link()
        time.sleep(2)
        selected_insurance = homepage.verify_selected_insurance()
        assert selected_insurance == "Camper Insurance", "Camper vehicle is not present"
