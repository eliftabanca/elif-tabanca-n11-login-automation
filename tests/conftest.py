import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.fixture(scope="function")
def setup(request, browser="chrome", environment="prod"):
    """Setup WebDriver with default browser and environment."""

    #Initialize WebDriver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError("Invalid browser! Supported browser: chrome")

    #Set base URL
    base_urls = {
        "prod": BASE_URL,
    }
    base_url = base_urls.get(environment, BASE_URL)

    #Open the browser and maximize window
    driver.get(base_url)
    driver.maximize_window()

    # Attach WebDriver and LoginPage to test class
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)  

    yield
    driver.quit()

