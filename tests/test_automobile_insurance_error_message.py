import datetime
import os
import time

import pytest
from dateutil.relativedelta import relativedelta

from Pages.InsurantDataPage import InsurantDataPage
from Pages.VehicleDataPage import VehicleDataPage
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestAutomobileInsurance:

    BASEPATH = os.path.dirname(os.path.abspath(__file__))

    def test_engine_performance_error_message(self):
        """
        Given:
            Land on Tricentis website
        When:
            1.Click on Automobile Header Link
            2.Enter Engine Performance greater than 2000
            3.Enter Engine Performance as 0
        Then:
            1. User should land on Vehicle Data Page
            2. Error Message Should be shown when Engine Performance is greater than 2000 :- "Must be a number between 1 and 2000"
            3. Error Message Should be shown when Engine Performance is less than 1 :- "Must be a number between 1 and 2000"
        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_engine_performance(test_data)
        error_message = vehicle_data_page.get_engine_performance_error_message()
        assert error_message == "Must be a number between 1 and 2000", "Wrong Error Message for Engine Performance"

        test_data['vehicle_Insurance_details']['vehicle_data']['Engine_Performance'] = 0
        vehicle_data_page.enter_engine_performance(test_data)
        error_message = vehicle_data_page.get_engine_performance_error_message()
        assert error_message == "Must be a number between 1 and 2000", "Wrong Error Message for Engine Performance"

    def test_price_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter List Price greater than 100000
                3.Enter List Price as 499
            Then:
                1. User should land on Vehicle Data Page
                2. Error Message Should be shown when List Price greater than 100000 :- "Must be a number between 500 and 100000"
                3. Error Message Should be shown when List Price is less than 500 :- "Must be a number between 500 and 100000"
        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_list_price(test_data)
        error_message = vehicle_data_page.get_list_price_error_message()
        assert error_message == "Must be a number between 500 and 100000", "Wrong Error Message for List Price"

        test_data['vehicle_Insurance_details']['vehicle_data']['List_Price'] = 499
        vehicle_data_page.enter_list_price(test_data)
        error_message = vehicle_data_page.get_list_price_error_message()
        assert error_message == "Must be a number between 500 and 100000", "Wrong Error Message for List Price"

    def test_annual_mileage_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter Annual Mileage greater than 100000
                3.Enter Annual Mileage as 99
            Then:
                1. User should land on Vehicle Data Page
                2. Error Message Should be shown when Annual Mileage greater than 100000 :- "Must be a number between 100 and 100000"
                3. Error Message Should be shown when Annual Mileage is less than 100 :- "Must be a number between 100 and 100000"
        """

        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_annual_mileage(test_data)
        error_message = vehicle_data_page.get_annual_mileage_error_message()
        assert error_message == "Must be a number between 100 and 100000", "Wrong Error Message for Annual Mileage"

        test_data['vehicle_Insurance_details']['vehicle_data']['Annual_Mileage'] = 99
        vehicle_data_page.enter_annual_mileage(test_data)
        error_message = vehicle_data_page.get_annual_mileage_error_message()
        assert error_message == "Must be a number between 100 and 100000", "Wrong Error Message for Annual Mileage"

    def test_first_name_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter first name as Number:-123
                5.Enter first name as Number:-A
            Then:
                1. User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error message should be displayed if First Name is Number :- "Must be at least 2 characters long and must only contain letters"
                5.Error message should be displayed if First Name is letter length is less than 2 :- "Must be at least 2 characters long and must only contain letters"
        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)
        insurance_data_page.enter_first_name(test_data)
        error = insurance_data_page.get_first_name_error_message()
        assert error == "Must be at least 2 characters long and must only contain letters"

        test_data['vehicle_Insurance_details']['Insurance_Data']['First_Name'] = "A"
        insurance_data_page.enter_first_name(test_data)
        error = insurance_data_page.get_first_name_error_message()
        assert error == "Must be at least 2 characters long and must only contain letters"

    def test_last_name_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter last name as Number:-123
                5.Enter last name as Number:-A
            Then:
                1. User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error message should be displayed if Last Name is Number :- "Must be at least 2 characters long and must only contain letters"
                5.Error message should be displayed if Last Name is letter length is less than 2 :- "Must be at least 2 characters long and must only contain letters"
        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)
        insurance_data_page.enter_last_name(test_data)
        error = insurance_data_page.get_last_name_error_message()
        assert error == "Must be at least 2 characters long and must only contain letters"

        test_data['vehicle_Insurance_details']['Insurance_Data']['Last_Name'] = "A"
        insurance_data_page.enter_last_name(test_data)
        error = insurance_data_page.get_last_name_error_message()
        assert error == "Must be at least 2 characters long and must only contain letters"

    def test_street_address_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter Street Address less than 3 character length
            Then:
                1. User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error should be shown when Street Address is less than 3 Character:- "Must be at least 3 characters long"

        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)
        insurance_data_page.enter_street_address(test_data)
        error = insurance_data_page.get_street_address_error_message()
        assert error == "Must be at least 3 characters long"

    def test_date_of_birth_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter Date Of Birth as less than 18
                5.Enter Date Of Birth Greater than 70
            Then:
                1. User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error message should be displayed if age is less than 18 :- "You must be between 18 and 70 years of age"
                5.Error message should be displayed if age is greater than 70:- "You must be between 18 and 70 years of age"

        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)

        sub_years = datetime.datetime.today() + relativedelta(years=-17)
        sub_years = sub_years.strftime("%m/%d/%Y")
        test_data['vehicle_Insurance_details']['Insurance_Data']['Date_Of_Birth'] = sub_years

        insurance_data_page.enter_date_of_birth(test_data)
        error = insurance_data_page.get_date_of_birth_error_message()
        assert error == "You must be between 18 and 70 years of age"

        add_years = datetime.datetime.today() + relativedelta(years=70)
        add_years = add_years.strftime("%m/%d/%Y")
        test_data['vehicle_Insurance_details']['Insurance_Data']['Date_Of_Birth'] = add_years

        insurance_data_page.enter_date_of_birth(test_data)
        error = insurance_data_page.get_date_of_birth_error_message()
        assert error == "You must be between 18 and 70 years of age"

    def test_zip_code_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter Zip Code as one digit
                5.Enter Zip Code greater than 8 digit
            Then:
                1.User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error message should be displayed if Zip Code is One Digit:-"Must be a number between 4 and 8 digits"
                5.Error message should be displayed if Zip Code is more than 8 Digit:-"Must be a number between 4 and 8 digits"

        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)

        insurance_data_page.enter_zip_code(test_data)
        error = insurance_data_page.get_zip_code_error_message()
        assert error == "Must be a number between 4 and 8 digits"
        time.sleep(2)

        test_data['vehicle_Insurance_details']['Insurance_Data']['Zip_Code'] = 123456789

        insurance_data_page.enter_zip_code(test_data)
        error = insurance_data_page.get_zip_code_error_message()
        assert error == "Must be a number between 4 and 8 digits"
        time.sleep(2)

    def test_website_error_message(self):
        """
            Given:
                Land on Tricentis website
            When:
                1.Click on Automobile Header Link
                2.Enter all details present on vehicle page
                3.click on next button and navigate to Insurance data page
                4.Enter Invalid Website
            Then:
                1.User should land on Vehicle Data Page
                2.User should be able to enter all details on vehicle page
                3.User should be navigate to Insurance Data Page Successfully
                4.Error message should be displayed for invalid website:-"Must be a valid URL"

        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_Validations.json")

        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)

        insurance_data_page.enter_website(test_data)
        error = insurance_data_page.get_website_error_message()
        assert error == "Must be a valid URL"
