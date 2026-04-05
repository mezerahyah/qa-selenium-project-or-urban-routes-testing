from selenium import webdriver
import data
import helpers



class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")
    supportive_plan = (By.XPATH, "//div[contains(@class, 'tcard') and contains(., 'Supportive')]")
    active_plan = (By.CSS_SELECTOR, ".tcard.active")
    phone_number_field = (By.ID, "phone")
    code_field = (By.ID, "code")
    message_for_driver_field = (By.ID, "message")
    comment_field = (By.ID, "comment")
    blanket_handkerchiefs_slider = (By.XPATH, "//div[@class='slider round']")
    blanket_handkerchiefs_checkbox = (By.ID, "blanket")
    ice_cream_plus_button = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter = (By.CLASS_NAME, "counter-value")

    def __init__(self, driver):
        self.driver = driver

    def set_from_address(self):
        self.driver.find_element(*self.from_field).send_keys(data.ddress_from)

    def set_to_address(self):
        self.driver.find_element(*self.to_field).send_keys(data.address_to)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan).click()

    def get_active_plan_text(self):
        return self.driver.find_element(*self.active_plan).text

    def click_phone_number_field(self):
        self.driver.find_element(*self.phone_number_field).click()

    def set_phone_number(self):
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def set_phone_code(self, code):
        self.driver.find_element(*self.phone_code_field).send_keys(code)

    def get_phone_number_value(self):
        return self.driver.find_element(*self.phone_number_field).get_property("value")


    def add_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)
        self.driver.find_element(*self.cvv_field).send_keys(data.card_code)
        self.driver.find_element(*self.cvv_field).send_keys(Keys.TAB)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.link_button))
        self.driver.find_element(*self.link_button).click()
        self.driver.find_element(*self.close_payment_modal).click()

    def set_message_for_driver(self):
        comment_element = self.driver.find_element(*self.comment_field)
        comment_element.clear()
        comment_element.send_keys(data.message_for_driver)


    def click_blanket_handkerchiefs_slider(self):
        self.driver.find_element(*self.blanket_handkerchiefs_slider).click()

    def is_blanket_handkerchiefs_selected(self):
        return self.driver.find_element(*self.blanket_handkerchiefs_checkbox).get_property('checked')

    def order_ice_creams(self):
        self.driver.find_element(*self.ice_cream_plus_button).click()
        self.driver.find_element(*self.ice_cream_plus_button).click()
            
    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ice_cream_counter).text)

    def set_route(self, address_from, address_to):
        set_address_from(self, address)
        self.driver.find_element(*self.from_field).send_keys(address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_tariff(self):
        self.driver.find_element(*self.supportive_plan).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def add_message_for_driver(self, message):
        comment_element = self.driver.find_element(*self.comment_field)
        comment_element.clear()
        comment_element.send_keys(data.message_for_driver)

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def is_car_search_modal_displayed(self):
        return self.driver.find_element(*self.car_search_modal_locator).is_displayed()
