import pytest
import allure
import time
from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageObjects.pom.dashboardPage import DashboardPage
from tests.pageObjects.pom.loginPage import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = Options()
    driver =webdriver.Chrome(options = options)
    options.add_argument("--headless")
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(Constants.login_url())
    return driver

@allure.epic("OrangeHRM Dashboard test")
@allure.feature("OrangeHRM Dashboard 'About' test")
@pytest.mark.positive
def test_orangehrm_about(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.login_to_hrm(usr="Admin",pwd="admin123")
    dashboard_page = DashboardPage(driver=driver)
    profile = dashboard_page.get_user_profile()
    about = dashboard_page.get_about_link().click()
    about_text = dashboard_page.get_about_text()
    assert about_text == "About"
    time.sleep(5)
