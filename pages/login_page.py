from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import *
from tests.conftest import *

class LoginPage(BasePage):
   

    # Actions
    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def clear_fields(self):
        self.enter_text(self.EMAIL_INPUT, "")
        self.enter_text(self.PASSWORD_INPUT, "")
