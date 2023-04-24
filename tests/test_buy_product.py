import sys; sys.path.append('../automation_project_1')
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time


def test_buy_product(driver):
    print("Start test")
    login = LoginPage(driver)
    login.authorization()
    time.sleep(3)
    mp = MainPage(driver)
    mp.select_product()
    time.sleep(3)