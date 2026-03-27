import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from demoqa.pages.application import Application


BASE_URL = "https://demoqa.com"


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")            # headless режим
    options.add_argument("--no-sandbox")              # для CI
    options.add_argument("--disable-dev-shm-usage")   # для CI
    options.add_argument("--disable-gpu")             # иногда нужно
    options.add_argument("--window-size=1920,1080")   # для правильного рендера

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = BASE_URL
    browser.config.timeout = 6

    yield

    driver.quit()


@pytest.fixture
def app():
    return Application()


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

