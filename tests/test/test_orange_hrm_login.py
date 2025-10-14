from webbrowser import Chrome

import pytest
import allure
import time
from selenium import webdriver
from tests.constants.constants import Constants
from selenium.webdriver.chrome.options import Options
from tests.pageObjects.pom.dashboardPage import DashboardPage
from tests.pageObjects.pom.loginPage import LoginPage


@pytest.fixture()
def setup():
    # options = Options()
    # driver =webdriver.Chrome(options = options)
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.login_url())
    return driver

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#0- OrangeHRM Login test- Positive")
@pytest.mark.positive
def test_orangehrm_login_positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Admin",pwd="admin123")
    dashboard_page = DashboardPage(driver=setup)
    dash_text = dashboard_page.get_dash_text()
    assert dash_text == "Dashboard"
    # login_page.get_change_url()


@allure.epic("OrangeHRM Login test")
@allure.feature("TC#1- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Ad",pwd="ad")
    error = login_page.get_error()
    assert error == "Invalid credentials"