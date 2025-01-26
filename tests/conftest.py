import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from utils.config import *

@pytest.fixture(scope="function")
def setup(request, browser="chrome", environment="prod"):
    """Setup WebDriver with default browser and environment."""

    # Initialize WebDriver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError("Invalid browser! Supported browser: chrome")

    # Set base URL
    base_urls = {
        "prod": BASE_URL,
    }
    base_url = base_urls.get(environment, BASE_URL)

    # Open the browser and maximize window
    driver.get(base_url)
    driver.maximize_window()

    # Attach WebDriver and LoginPage to test class
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)  # LoginPage otomatik hazır

    yield
    driver.quit()




# @pytest.fixture(scope="function")
# def setup(request, browser="chrome", environment="prod"):
#     """Setup WebDriver with default browser and environment."""

#     # Initialize WebDriver
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         raise ValueError("Invalid browser! Supported browsers: chrome, firefox")

#     # Set base URL
#     base_urls = {
#         "dev": "https://dev-n11.com",
#         "qa": "https://qa-n11.com",
#         "pre-prod": "https://preprod-n11.com",
#         "prod": BASE_URL,
#     }
#     base_url = base_urls.get(environment, BASE_URL)

#     # Open the browser and maximize window
#     driver.get(base_url)
#     driver.maximize_window()

#     # Attach WebDriver and base URL to test class
#     request.cls.driver = driver
#     request.cls.baseurl = base_url

#     yield
#     driver.quit()
