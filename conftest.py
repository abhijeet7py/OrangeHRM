import pytest
import allure
from tests.utils.driver_factory import get_driver
from tests.config.config_reader import get_config

@pytest.fixture(scope="function")
def driver():
    config = get_config()

    driver = get_driver(config["browser"])
    driver.get(config["base_url"])
    driver.maximize_window()
    yield driver
    driver.quit()


# Hook for screenshot failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name= "failure",
                attachment_type=allure.attachment_type.PNG,
            )