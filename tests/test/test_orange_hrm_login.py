import pytest
import allure
import time
from selenium import webdriver
from tests.config.constants import Constants
from selenium.webdriver.chrome.options import Options
from tests.pageObjects.pom.dashboardPage import DashboardPage
from tests.pageObjects.pom.loginPage import LoginPage


@allure.epic("OrangeHRM Login test")
@allure.feature("TC#1- OrangeHRM Login test- Positive")
@pytest.mark.positive
def test_orangehrm_login_positive(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Admin",pwd="admin123")
    dashboard_page = DashboardPage(driver=driver)
    dash_text = dashboard_page.get_dash_text()
    assert dash_text == "Dashboard"
    # login_page.get_change_url()


@allure.epic("OrangeHRM Login test")
@allure.feature("TC#2- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_1(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Ad",pwd="ad")
    error = login_page.get_error()
    assert error == "Invalid credentials"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#3- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_2(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="",pwd="admin123")
    req_error = login_page.get_usr_req()
    assert req_error == "Required"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#4- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_3(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Admin",pwd="")
    req_error = login_page.get_pass_req()
    assert req_error == "Required"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#5- OrangeHRM Login test- Negative")
@pytest.mark.negative
def test_orangehrm_login_negative_4(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Admin",pwd="sd")
    error = login_page.get_error()
    assert error == "Invalid credentials"

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#6- OrangeHRM Login test- Positive")
@pytest.mark.negative
def test_orangehrm_login_negative_5(driver):
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Adm",pwd="admin123")
    error = login_page.get_error()
    assert error == "Invalid credentials"

@allure.epic("OrangeHRM Logout test")
@allure.feature("TC#7- OrangeHRM Login test- Positive")
@pytest.mark.positive
def test_logout_hrm(driver):
    driver = driver
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Admin",pwd="admin123")
    dashboard_page = DashboardPage(driver=driver)
    profile = dashboard_page.get_user_profile()
    logout = dashboard_page.get_logout_button().click()
    current = driver.current_url
    expected = Constants.login_url()
    assert f"Expected URL {expected} but got {current}."
    print(current)
