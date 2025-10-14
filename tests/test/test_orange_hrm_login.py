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
    options = Options()
    driver =webdriver.Chrome(options = options)
    options.add_argument("--headless")
    # driver = webdriver.Chrome()
    # driver.maximize_window()
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
def test_orangehrm_login_negative_1(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Ad",pwd="ad")
    error = login_page.get_error()
    assert error == "Invalid credentials"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#2- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_2(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="",pwd="admin123")
    req_error = login_page.get_usr_req()
    assert req_error == "Required"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#3- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_3(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Admin",pwd="")
    req_error = login_page.get_pass_req()
    assert req_error == "Required"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#4- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_4(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Admin",pwd="sd")
    error = login_page.get_error()
    assert error == "Invalid credentials"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#5- OrangeHRM Login test- Positive")
@pytest.mark.negative
def test_orangehrm_login_negative_5(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Adm",pwd="admin123")
    error = login_page.get_error()
    assert error == "Invalid credentials"