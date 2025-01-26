from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default timeout of 10 seconds

    def open_url(self, url):
        self.driver.get(url)

    # # Waits for an element to be present and returns it
    # def find_element(self, locator, timeout=10):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.presence_of_element_located(locator))
    
    
    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return element
    
    def wait_element_presence(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return element
   
    def wait_element_clickable(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return element
    

    def click_element(self, locator): #checks both: clickable and clicks

         element = self.wait.until(EC.element_to_be_clickable(locator))
         element.click()

    def enter_text(self, locator, text):
        # Waits for an element to be present and enters the specified text
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        # Waits for an element to be present and returns its text
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
    
    def get_URL(self):
        return self.driver.current_url
