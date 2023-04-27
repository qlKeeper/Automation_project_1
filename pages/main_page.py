from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(Base):
    
    # Locators
    product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'
    menu_btn = '//button[@id="react-burger-menu-btn"]'
    about_link = '//a[@id="about_sidebar_link"]'

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    
    def get_product_2(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.product_2)))
    
    def get_product_3(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.product_3)))
    
    def get_cart(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    
    def get_menu(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.menu_btn)))
    
    def get_about_link(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.about_link)))
    
    # Actions
    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click select product 1")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Click select product 1")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Click select product 1")

    def click_cart(self):
        self.get_cart().click()
        print("Enter the cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_about_link(self):
        self.get_about_link().click()

    # Methods
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about_link()
        self.assert_url('https://saucelabs.com/')