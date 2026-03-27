import pytest
from selene import browser
from selenium import webdriver

from demoqa.pages.application import Application

BASE_URL = "https://demoqa.com"


# @pytest.fixture(autouse=True)
# def browser_setup():
#     browser.config.driver = webdriver.Chrome()
#     browser.config.base_url = BASE_URL
#     browser.driver.maximize_window()
#     # browser.config.window_width = '1920'
#     # browser.config.window_height = '1080'
#     browser.config.headless = False
#     browser.config.browser_name = "chrome"
#     browser.config.timeout = 6

#     yield
#     browser.close()

@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"

    yield

    driver.quit()


@pytest.fixture
def app():
    return Application()
