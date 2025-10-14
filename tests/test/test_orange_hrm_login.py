import pytest
import allure
import time
from selenium import webdriver
from tests.constants.constants import Constants
from selenium.webdriver.chrome.options import Options

from tests.pageObjects.pom.loginPage import LoginPage


@pytest.fixture()
def setup():
    options = Options()
    driver =webdriver.Chrome(options=options)
    options.add_argument("--start-maximized")
    driver.get(Constants.login_url())
    return driver

@allure.epic("OrangeHRM Login test")
@allure.feature("TC#0- OrangeHRM Login test- Positive")
@pytest.mark.positive
def test_OrangeHRM_Login_Positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_hrm(usr="Admin",pwd="admin123")