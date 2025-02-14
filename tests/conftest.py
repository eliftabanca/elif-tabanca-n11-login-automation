import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.base_page import BasePage
from datetime import datetime
from utils.config import BASE_URL

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(scope="function")
def setup(request, browser="chrome", environment="prod", headless=None):
  
    
   
    if headless is None:
        headless = sys.platform.startswith("linux")  #Enable headless mode on GitHub Actions

    if browser == "chrome":
        chrome_options = Options()

        if headless:
            chrome_options.add_argument("--headless")

        chrome_options.add_argument("--no-sandbox")  
        chrome_options.add_argument("--disable-dev-shm-usage")  
        chrome_options.add_argument("--disable-gpu")  
        chrome_options.add_argument("--remote-debugging-port=9222")  
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data") 

        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        except Exception as e:
            print(f" WebDriver failed to initialize: {e}")
            pytest.fail(f"WebDriver Error: {e}")
    else:
        raise ValueError("⚠️ Invalid browser! Only 'chrome' is supported.")

    base_urls = {"prod": BASE_URL}
    base_url = base_urls.get(environment, BASE_URL)

    driver.get(base_url)
    driver.implicitly_wait(20)  

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(("id", "login-button")) 
        )
    except Exception as e:
        print(f"Page did not load properly: {e}")

    try:
        base_page = BasePage(driver)
        base_page.accept_cookies()
        base_page.accept_notifications()
    except Exception as e:
        print(f"BasePage initialization failed: {e}")

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
    print(f" Screenshot saved: {screenshot_path}")

    driver.quit()
