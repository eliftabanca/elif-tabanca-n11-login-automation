import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from pages.login_page import LoginPage
from pages.base_page import BasePage
from utils.config import BASE_URL

def start_webdriver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

@pytest.fixture(scope="function")
def setup(request):
    driver = start_webdriver()
    driver.get(BASE_URL)
    
    base_page = BasePage(driver)
    request.cls.driver = driver
    request.cls.base_page = base_page
    request.cls.login_page = LoginPage(driver)
    
    yield driver

    take_screenshot(driver, request.node.name)
    driver.quit()
