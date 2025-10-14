from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.utils.common_utils import webdriver_wait,wedriver_wait_url

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    dash = (By.XPATH,"//h6[normalize-space()='Dashboard']")

    def get_dash(self):
        return self.driver.find_element(*DashboardPage.dash)


    # Page Action
    def get_dash_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.dash, timeout=10)
        return self.get_dash().text
