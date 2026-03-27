# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager

from demoqa.pages.application import Application

BASE_URL = "https://demoqa.com"


@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.driver = webdriver.Chrome()
    browser.config.base_url = BASE_URL
    browser.driver.maximize_window()
    # browser.config.window_width = '1920'
    # browser.config.window_height = '1080'
    browser.config.headless = False
    browser.config.browser_name = "chrome"
    browser.config.timeout = 6

    yield
    browser.close()


@pytest.fixture
def app():
    return Application()
