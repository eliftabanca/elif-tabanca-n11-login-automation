from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.config import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  

    def open_url(self, url):
        self.driver.get(url)
        self.wait_for_page_load()  

    def wait_element_visibility(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.take_screenshot("wait_element_visibility")
            raise

    def wait_element_presence(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.take_screenshot("wait_element_presence")
            raise
    
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            self.take_screenshot("click_element")
            raise

    def wait_element_clickable(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Timeout: Element {locator} is not clickable!")
            self.take_screenshot("wait_element_clickable")
            raise

    def enter_text(self, locator, text):
        try:
            element = self.wait_element_visibility(locator)  
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Timeout: Unable to enter text in {locator}")
            self.take_screenshot("enter_text")
            raise

    def get_text(self, locator):
        try:
            return self.wait_element_visibility(locator).text
        except TimeoutException:
            print(f"Timeout: Unable to retrieve text from {locator}")
            self.take_screenshot("get_text")
            raise

    def take_screenshot(self, filename="screenshot"):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join("screenshots", f"{filename}_{timestamp}.png")

        self.driver.save_screenshot(file_path)
        print(f" Screenshot saved at: {file_path}")
        return file_path

    def get_title(self):

        return self.driver.title

    def get_URL(self):
        return self.driver.current_url

    def wait_for_page_load(self, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print("Page fully loaded.")
        except TimeoutException:
            self.take_screenshot("wait_for_page_load")
            raise
