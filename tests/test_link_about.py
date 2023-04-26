import time
from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_link_about(driver):

    login = LoginPage(driver)
    login.authorization()
    time.sleep(1)
    
    mp = MainPage(driver)
    mp.select_menu_about()
    time.sleep(1)

    print('Finish test')