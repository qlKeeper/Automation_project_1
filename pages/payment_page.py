from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PaymentPage(Base):

    # Locators
    finish_btn = '//button[@id="finish"]'

    # Getters
    def get_finish_btn(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.finish_btn)))
    
    
    # Actions
    def click_finish_btn(self):
        self.get_finish_btn().click()
        print("Click finish button")

    
    # Methods
    def payment(self):
        self.get_current_url()
        self.click_finish_btn()
