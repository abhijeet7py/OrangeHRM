from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.utils.common_utils import webdriver_wait,wedriver_wait_url
from tests.pageObjects.pom.loginPage import LoginPage

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    dash = (By.XPATH,"//h6[normalize-space()='Dashboard']")
    user_profile = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    logout_button = (By.XPATH,"//a[normalize-space()='Logout']")
    about_link = (By.XPATH,"//a[normalize-space()='About']")
    about_text = (By.XPATH,"//h6[normalize-space()='About']")

    def get_dash(self):
        return self.driver.find_element(*DashboardPage.dash)
    def get_user_profile(self):
        webdriver_wait(driver = self.driver, element_tuple=self.user_profile,timeout=5)
        return self.driver.find_element(*DashboardPage.user_profile).click()
    def get_logout_button(self):
        webdriver_wait(driver=self.driver,element_tuple=self.logout_button ,timeout=5)
        return self.driver.find_element(*DashboardPage.logout_button)
    def get_about_link(self):
        return self.driver.find_element(*DashboardPage.about_link)


    # Page Action
    def get_dash_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.dash, timeout=10)
        return self.get_dash().text

    def get_about_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.about_text,timeout=5)
        return self.driver.find_element(*DashboardPage.about_text).text





