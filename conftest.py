from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def set_up():
    print("Start test (set_up)")
    yield
    print("Finish test (set_up)")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")