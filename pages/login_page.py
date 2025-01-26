from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import *
from pages.base_page import *


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
   
    
    def enter_email(self, data):
        user_name = self.wait_element_visibility(EMAIL_INPUT)
        user_name.clear()
        user_name.send_keys(data)

    
    def enter_password(self, data):
        user_password = self.wait_element_visibility(PASSWORD_INPUT)
        user_password.clear()
        user_password.send_keys(data)
    

    def click_loginButton(self):
        self.wait_element_clickable(LOGIN_BUTTON_LOCATOR).click()

    def logo_title_find(self):
        logo_title = self.wait_element_visibility(LOGO_LOCATOR)
        return logo_title.text

    def get_error_message(self):
        error_message_element = self.wait_element_visibility(ERROR_MESSAGE_INVALID_CREDENTIALS_LOCATOR)
        return error_message_element.text
    
    def get_email_error_message(self):
        email_error_element = self.wait_element_visibility(ERROR_MESSAGE_EMPTY_EMAIL_LOCATOR)
        return email_error_element.text

    def get_password_error_message(self):
         password_error_element = self.wait_element_visibility(ERROR_MESSAGE_EMPTY_PASSWORD_LOCATOR)
         return password_error_element.text
    
   
   