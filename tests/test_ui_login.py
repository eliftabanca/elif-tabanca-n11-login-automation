import pytest
import softest
from pages.login_page import LoginPage
from utils.config import *

@pytest.mark.usefixtures("setup")  
class TestResponsiveLoginUI(softest.TestCase):
   
    def test_mobile_ui_elements(self):
        self.driver.set_window_size(375, 667)  
        email_field = self.driver.find_element(*self.login_page.email_field)
        email_size = email_field.size
        email_location = email_field.location

        self.assertTrue(300 <= email_size['width'] <= 400, "Email field width is not as expected for iPhone SE")
        self.assertTrue(40 <= email_size['height'] <= 50, "Email field height is not as expected for iPhone SE")
        self.assertTrue(email_location['y'] > 100, "Email field Y position is not as expected for iPhone SE")

        print("✅ Mobile UI test passed for iPhone SE.")

    def test_tablet_ui_elements(self):
        self.driver.set_window_size(768, 1024)

        email_field = self.driver.find_element(*self.login_page.email_field)
        email_size = email_field.size
        email_location = email_field.location

        self.assertTrue(400 <= email_size['width'] <= 500, "Email field width is not as expected for iPad Mini")
        self.assertTrue(40 <= email_size['height'] <= 50, "Email field height is not as expected for iPad Mini")
        self.assertTrue(email_location['y'] > 100, "Email field Y position is not as expected for iPad Mini")

        print("✅ Tablet UI test passed for iPad Mini.")
