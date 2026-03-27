# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://demoqa.com"

@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    # Настройки Chrome
    options = Options()
    options.add_argument("--headless=new")  # headless для новых версий Chrome
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Инициализация ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Настройка Selene
    browser.config.driver = driver
    browser.config.base_url = BASE_URL
    browser.driver.maximize_window()
    # browser.config.window_width = '1920'
    # browser.config.window_height = '1080'
    browser.config.headless = True
    browser.config.browser_name = "chrome"
    browser.config.timeout = 6

    yield browser

    driver.quit()


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

