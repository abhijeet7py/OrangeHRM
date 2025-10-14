# login page class
from selenium.webdriver.common.by import By

from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait,wedriver_wait_url
# Page locators
# Page Actions

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    username = (By.XPATH,"//input[@class='oxd-input oxd-input--active' and @name='username']")
    password = (By.XPATH,"//input[@class='oxd-input oxd-input--active' and @name='password']")
    login = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    err_text = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    usr_req_txt = (By.XPATH,"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    pass_req_text = (By.XPATH,"//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")


    # Page Actions -> You need to write the functions to access them

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
            # * --> means current class
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login)
    def get_err_text(self):
        webdriver_wait(driver=self.driver, element_tuple = self.err_text, timeout=5)
        return self.driver.find_element(*LoginPage.err_text)
    def get_usr_req_text(self):
        webdriver_wait(driver= self.driver, timeout=5,element_tuple=self.usr_req_txt)
        return self.driver.find_element(*LoginPage.usr_req_txt)
    def get_pass_req_text(self):
        webdriver_wait(driver=self.driver, timeout=5, element_tuple=self.pass_req_text)
        return self.driver.find_element(*LoginPage.pass_req_text)

    def login_to_hrm(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys()
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
        expected_url = Constants.dashboard_url()
        wedriver_wait_url(driver=self.driver,timeout=5)
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"
