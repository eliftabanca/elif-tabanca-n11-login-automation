from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default timeout of 10 seconds
#Opens the specified URL.
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        """#Waits for an element to be present and returns it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Waits for elements to be present and returns them."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        #Waits for an element to be clickable and clicks it.
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Waits for an element to be present and enters the specified text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Waits for an element to be present and returns its text."""
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """Checks if an element is visible on the page."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_present(self, locator):
        """Checks if an element is present in the DOM."""
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def wait_for_element_disappear(self, locator):
        """Waits for an element to disappear."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def take_screenshot(self, filename="screenshot"):
        """Takes a screenshot and saves it to the 'screenshots' directory."""
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join("screenshots", f"{filename}_{timestamp}.png")

        # Save the screenshot
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved to {file_path}")
        return file_path
