import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.base_page import BasePage
from datetime import datetime
import os
from utils.config import *

@pytest.fixture(scope="function")
def setup(request, browser="chrome", environment="prod"):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError("Invalid browser! Supported browser: chrome")

    base_urls = {"prod": BASE_URL}
    base_url = base_urls.get(environment, BASE_URL)

    driver.get(base_url)
    driver.maximize_window()

    base_page = BasePage(driver)
    try:
        base_page.accept_cookies()
        base_page.accept_notifications()
    except Exception as e:
        print(f": {e}")

    request.cls.driver = driver
    request.cls.base_page = base_page
    request.cls.login_page = LoginPage(driver)

    yield

    # Her testten sonra ekran görüntüsü alma
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshots_dir = "screenshots"

    # Ekran görüntüsü için klasör oluştur
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Scrrenshot added: {screenshot_path}")

    driver.quit()
