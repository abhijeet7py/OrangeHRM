# Page Locators
# Page Actions
# Webdriver init
# Custom Functions
# No assertions here ( these are not test cases)

from seleniumpagefactory.Pagefactory import PageFactory
from tests.utils.common_utils import webdriver_wait, wedriver_wait_url
from selenium.webdriver.common.by import By

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True


    # Page locators (Create a dictionary)
    locators = {
        'username': ('XPATH', "//input[@placeholder='Username']"),
        'password': ('XPATH',"//input[@placeholder='Password']"),
        'login': ('XPATH',"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"),
        'err_text':('XPATH',"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"),
        'usr_req_txt':('XPATH',"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]"),
        'pass_req_text':('XPATH',"//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")
    }

    def login_to_hrm(self,usr,pwd):
        self.username.set_text(usr)
        self.password.set_text(pwd)
        self.login.click_button()

    def error_text(self):
        return self.err_text.get_text()

    def user_req_text(self):
        return self.usr_req_txt.get_text()

    def pas_req_text(self):
        return self.pass_req_text.get_text()



