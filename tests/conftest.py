import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config import *

@pytest.fixture(scope="function")
def setup(request, browser=None, environment=None):
    
    # Set default browser if not provided
    if browser is None:
        browser = "chrome"
    
    # Set default environment if not provided
    if environment is None:
        environment = "prod"
    
    # Initialize WebDriver based on browser choice
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Invalid browser! Supported browsers: chrome, firefox")

    # Set the base URL based on environment
    if environment == "dev":
        base_url = "https://dev-tobeto.com"
    elif environment == "qa":
        base_url = "https://qa-tobeto.com"
    elif environment == "pre-prod":
        base_url = "https://preprod-tobeto.com"
    elif environment == "prod":
        base_url = BASE_URL
    else:
        raise ValueError("Invalid environment! Supported environments: dev, qa, pre-prod, prod")

    # Open the browser and maximize window
    driver.get(base_url)
    driver.maximize_window()

    # Attach driver and base URL to the test class
    request.cls.driver = driver
    request.cls.baseurl = base_url

    yield
    driver.quit()
