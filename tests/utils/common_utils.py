# Try to add all the possible waits

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants.constants import Constants

# Here we are using method overloading concept
# method overloading means using same name functions with different arguments

def webdriver_wait(driver,element_tuple):
    WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located(element_tuple))

def webdriver_wait(driver,element_tuple,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(
        EC.visibility_of_element_located(element_tuple))

def wedriver_wait_url(driver,timeout):
    WebDriverWait(driver = driver, timeout = timeout).until(
        EC.url_changes(Constants.dashboard_url()))