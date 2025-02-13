import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.base_page import BasePage
from datetime import datetime
import os
from utils.config import *

@pytest.fixture(scope="function")
def setup(request, browser="chrome", environment="prod"):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")  # CI/CD'de güvenli çalıştırma
        chrome_options.add_argument("--disable-dev-shm-usage")  # Bellek sorunlarını önler
        chrome_options.add_argument("--headless")  # CI/CD için headless mod
        chrome_options.add_argument("--disable-gpu")  # GPU kullanımını kapat
        chrome_options.add_argument("--remote-debugging-port=9222")  # Çakışmayı önler
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Kullanıcı verisi çakışmasını önler

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
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
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshots_dir = "screenshots"

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot added: {screenshot_path}")

    driver.quit()
