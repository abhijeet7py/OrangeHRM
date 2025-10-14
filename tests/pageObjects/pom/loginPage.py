# login page class
from selenium.webdriver.common.by import By

from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait,wedriver_wait_url
# Page locators
# Page Actions
# web driver initialization
# Custom functions
# No assertions (Page object class)

class LoginPage:
    # Adding parameterized constructor
    def __init__(self,driver):
        self.driver = driver

    # Page Locators tuples
    username = (By.XPATH,"//input[@placeholder='Username']")
    password = (By.XPATH,"//input[@placeholder='Password']")
    login = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    err_text = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    usr_req_txt = (By.XPATH,"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    pass_req_text = (By.XPATH,"//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")


    # Page Actions -> You need to write the functions to access Page locator tuples

    def get_username(self):
        webdriver_wait(driver=self.driver,element_tuple=self.username,timeout=10)
        return self.driver.find_element(*LoginPage.username)
            # * --> means current class
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login)
    def get_err_text(self):
        webdriver_wait(driver=self.driver, element_tuple = self.err_text, timeout=10)
        return self.driver.find_element(*LoginPage.err_text)
    def get_usr_req_text(self):
        webdriver_wait(driver= self.driver, timeout=5,element_tuple=self.usr_req_txt)
        return self.driver.find_element(*LoginPage.usr_req_txt)
    def get_pass_req_text(self):
        webdriver_wait(driver=self.driver, timeout=5, element_tuple=self.pass_req_text)
        return self.driver.find_element(*LoginPage.pass_req_text)

    # Page action --> Main action
    def login_to_hrm(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_login_button().click()
        except Exception as e:
            print(e)

    def get_error(self):
        return self.get_err_text().text
    def get_usr_req(self):
        return self.get_usr_req_text().text
    def get_pass_req(self):
        return self.get_pass_req_text().text
    def get_change_url(self):
        wedriver_wait_url(driver=self.driver,timeout=5)
        expected_url = Constants.dashboard_url()
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"

