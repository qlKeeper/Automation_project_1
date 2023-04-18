import sys; sys.path.append('../automation_project_1')
from selenium import webdriver
from pages.login_page import LoginPage
import time


def test_authorization():
    driver = webdriver.Chrome()
    print("Start test")

    login = LoginPage(driver)
    login.authorization()
    time.sleep(3)