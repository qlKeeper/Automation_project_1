import sys; sys.path.append('../automation_project_1')
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time


def test_buy_product(driver):
    print("Start test")
    
    login = LoginPage(driver)
    login.authorization()
    time.sleep(1)
    
    mp = MainPage(driver)
    mp.select_product()
    time.sleep(1)

    cp = CartPage(driver)
    cp.click_checkout_button()
    time.sleep(1)