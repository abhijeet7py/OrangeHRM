from selenium import webdriver

def get_driver(browser):

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return  webdriver.Chrome(options = options)

    elif browser.lower() == "firefox":
        return webdriver.Firefox()

    elif browser.lower() == "safari":
        return webdriver.Safari()

    else:
        raise Exception(f"Unsupported browser {browser}")