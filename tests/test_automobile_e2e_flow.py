import os

import pytest

from Pages.HomePage import HomePage
from Pages.InsurantDataPage import InsurantDataPage
from Pages.PriceOptionPage import PriceOptionPage
from Pages.ProductDataPage import ProductDataPage
from Pages.Send_Quote_Page import SendQuotePage
from Pages.VehicleDataPage import VehicleDataPage


@pytest.mark.usefixtures("setup")
class TestAutomobileInsurance:

    BASEPATH = os.path.dirname(os.path.abspath(__file__))

    def test_automobile_e2e_flow(self):
        """
        Given:
            Land on Tricentis website
        When:
            1.Click on Automobile Header Link
            2.Enter all details on Vehicle Data Page
            3.Enter all details on Insurant Data Page
            4.Enter all details on product data page
            5.select price
            6.send Quote
        Then:
            1. User should land on Vehicle Data Page
            2. User should be able to enter all data on vehicle data page
            3. User should be able to enter all data on Insurant data page
            4. User should be able to enter all data on Product data page
            5. User should be able to select Price
            6. User should be able to send a quote
        """
        homepage = HomePage(self.driver)
        vehicle_data_page = VehicleDataPage(self.driver)
        insurance_data_page = InsurantDataPage(self.driver)
        product_data_page = ProductDataPage(self.driver)
        price_option_page = PriceOptionPage(self.driver)
        send_quote_page = SendQuotePage(self.driver)

        test_data = homepage.get_test_data(self.BASEPATH, "AutomobileInsurance_e2e_flow.json")
        homepage.click_automobile_header_link()
        vehicle_data_page.enter_vehicle_data(test_data)
        insurance_data_page.enter_insurance_date(test_data)
        product_data_page.enter_product_data(test_data)
        price_option_page.select_price_option(test_data)
        price_option_page.click_next_button()
        send_quote_page.enter_send_quote_details(test_data)
