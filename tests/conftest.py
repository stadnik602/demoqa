import pytest
from selene import browser

BASE_URL = 'https://demoqa.com'

@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.base_url = BASE_URL
    browser.driver.maximize_window()
    # browser.config.window_width = '1920'
    # browser.config.window_height = '1080'
    browser.config.headless = False
    browser.config.browser_name = 'chrome'
    browser.config.timeout = 6

    yield
    browser.close()

