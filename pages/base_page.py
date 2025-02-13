from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from utils.config import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  

    def open_url(self, url):
        self.driver.get(url)


    def wait_element_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def take_screenshot(self, filename="screenshot"):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join("screenshots", f"{filename}_{timestamp}.png")

        # Save the screenshot
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved to {file_path}")
        return file_path

    def get_title(self):
        return self.driver.title
    
    def accept_cookies(self):
        try:
            accept_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)
            )
            accept_button.click()
     
        except Exception as e:
            print(f"Failed to accept cookies or notifications: {e}")

    def accept_notifications(self):
        try:
            accept_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(NOTIFICATION_ACCEPT_BUTTON)
            )
            accept_button.click()
        except Exception as e:
            print(f"Failed to accept cookies or notifications: {e}")
    
    def get_URL(self):
        return self.driver.current_url
