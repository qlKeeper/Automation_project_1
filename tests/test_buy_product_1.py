import sys; sys.path.append('../automation_project_1')
from pages.client_information_page import ClientInformationPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.finish_page import Finish_page
import time, pytest

# @pytest.mark.run(order=3)
def test_buy_product_1(driver):
    print("Start test 1")
    
    login = LoginPage(driver)
    login.authorization()
    time.sleep(1.5)
    
    mp = MainPage(driver)
    mp.select_product_1()
    time.sleep(1.5)

    cp = CartPage(driver)
    cp.click_checkout_button()
    time.sleep(1.5)

    cip = ClientInformationPage(driver)
    cip.input_information()
    time.sleep(1.5)

    p = PaymentPage(driver)
    p.click_finish_btn()
    time.sleep(1.5)

    f = Finish_page(driver)
    f.finish()
    time.sleep(1.5)

# @pytest.mark.run(order=1)
def test_buy_product_2(driver):
    print("Start test 2")
    
    login = LoginPage(driver)
    login.authorization()
    time.sleep(1.5)
    
    mp = MainPage(driver)
    mp.select_product_2()
    time.sleep(1.5)

    cp = CartPage(driver)
    cp.click_checkout_button()
    time.sleep(1.5)

# @pytest.mark.run(order=2)
def test_buy_product_3(driver):
    print("Start test 3")
    
    login = LoginPage(driver)
    login.authorization()
    time.sleep(1.5)
    
    mp = MainPage(driver)
    mp.select_product_3()
    time.sleep(1.5)

    cp = CartPage(driver)
    cp.click_checkout_button()
    time.sleep(1.5)