from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ClientInformationPage(Base):
    
    # Locators
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_btn = '//*[@id="continue"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    
    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))

    # Actions
    def input_first_name(self, first_name: str):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name: str):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code: str):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_btn(self):
        self.get_continue_btn().click()
        print("Continue button click")

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name('Pasha')
        self.input_last_name('Rogov')
        self.input_postal_code('117405')
        self.click_continue_btn()