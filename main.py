from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import data
import helpers

@classmethod
def setup_class(cls):
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    cls.driver = webdriver.Chrome()
    if helpers.is_url_reachable():
        data.URBAN_ROUTES_URL
        print("Connected to the Urban Routes server")
    else:
        print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route():
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.navigate_to_urban_routes()
        routes_page.set_address_from()
        routes_page.set_address_to()
    actual_address_from = routes_page.get_address_from()
    actual_address_to = routes_page.get_address_to()
    assert actual_from == data.address_from
    assert actual_to == data.address_to

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        active_plan_text = routes_page.get_active_plan_text()
    assert "Supportive" in active_plan_text

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_phone_number_field()
        phone_number = retrieve_phone_number(self.driver)
        routes_page.set_phone_number(phone_number)
    displayed_phone = routes_page.get_phone_number_value()
    assert data.phone_number in displayed_phone

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan
        routes_page.click_payment_method_field()
        routes_page.set_card_number()
        card_number = retrieve_card_bumber(self.driver)
    displayed_phone = routes.page.get_card_number_value()
    assert data.card_number in displayed_phone 
        
    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.set_message_for_driver()
    displayed_phone = routes.page.get.message_for_driver_text()
    assert date.message_for_driver in displayed_phone
    
    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.click_blanket_handkerchiefs()    
    assert routes_page.is_blanket_handkerchiefs_selected()
        
    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address_from()
        routes_page.set_address_to()
        routes_page.click_call_taxi_button()
        routes_page.order_ice_creams(2)
        for count in range(number_of_ice_creams):
           routes_page.click_ice_cream_button()     
    assert routes_page.get_ice_cream_count() == 2

    def test_car_search_model_appears(self):
        
        actual_from = routes_page.get_car_search_modal_text()
        assert actual_from == data.car_search_modal_text

@classmethod
def teardown_class(cls):
    cls.driver.quit()
