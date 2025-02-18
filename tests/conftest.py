import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from pages.login_page import LoginPage
from pages.base_page import BasePage
from utils.config import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=sys.platform.startswith("linux"), help="Run tests in headless mode")

def start_webdriver(headless):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    except Exception as e:
        pytest.fail(f"WebDriver initialization failed: {e}")
    
    return driver

def wait_for_element(driver, locator, timeout=15):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except Exception as e:
        print(f"⚠️ Element {locator} did not load: {e}")

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved: {screenshot_path}")

@pytest.fixture(scope="function")
def setup(request):
    headless = request.config.getoption("--headless")
    driver = start_webdriver(headless)
    driver.get(BASE_URL)
    driver.implicitly_wait(10)

    wait_for_element(driver, LOGIN_BUTTON_LOCATOR)
    
    base_page = BasePage(driver)


    try:
        base_page.accept_cookies()
    except Exception as e:
        print(f"Cookies modal could not be closed: {e}")

    try:
        base_page.accept_notifications()
    except Exception as e:
        print(f"Notifications modal could not be closed: {e}")
    
    request.cls.driver = driver
    request.cls.base_page = base_page
    request.cls.login_page = LoginPage(driver)
    
    yield

    take_screenshot(driver, request.node.name)
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    

    if report.failed:
        take_screenshot(item.cls.driver, item.nodeid.replace("/", "_").replace(":", "_"))
    
    setattr(item, "rep_" + report.when, report)
