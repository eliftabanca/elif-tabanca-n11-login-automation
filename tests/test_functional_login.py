import time
import pytest
import softest
from utils.config import *


@pytest.mark.usefixtures("setup")
class TestLogin(softest.TestCase):
    

    def test_valid_login(self):
        self.login_page.enter_email(VALID_USER_EMAIL) 
        self.login_page.enter_password(VALID_USER_PASSWORD)
        self.login_page.click_loginButton()
        actual_value = self.login_page.logo_title_find()
        self.soft_assert(self.assertEqual, LOGO_TITLE_TEXT, actual_value, "The title does not match the expected value.")
        self.assert_all()

    def test_invalid_username(self):
        self.login_page.enter_email(INVALID_USER_EMAIL)  
        self.login_page.enter_password(VALID_USER_PASSWORD) 
        self.login_page.click_loginButton()  
        actual_message = self.login_page.get_error_message()
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_INVALID_CREDENTIALS, actual_message, "Error message is not as expected.")
        self.assert_all()

    def test_invalid_password(self):
        self.login_page.enter_email(VALID_USER_EMAIL)
        self.login_page.enter_password(INVALID_USER_PASSWORD)  
        self.login_page.click_loginButton()  
        actual_message = self.login_page.get_error_message()  
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_INVALID_CREDENTIALS, actual_message, "Error message is not as expected.")
        self.assert_all()

    def test_empty_username_and_password(self): 
        self.login_page.click_loginButton()  
        email_error = self.login_page.get_email_error_message()
        password_error = self.login_page.get_password_error_message()
        
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_EMPTY_EMAIL, email_error, "Email error message is not as expected.")
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_EMPTY_PASSWORD, password_error, "Password error message is not as expected.")
        self.assert_all()

    def test_only_username_filled(self):
        self.login_page.enter_email(VALID_USER_EMAIL)  
        self.login_page.click_loginButton()  
        password_error = self.login_page.get_password_error_message()
        
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_EMPTY_PASSWORD, password_error, "Password error message is not as expected.")
        self.assert_all()
    
    def test_only_password_filled(self):
        self.login_page.enter_password(VALID_USER_PASSWORD)  
        self.login_page.click_loginButton()  
        email_error = self.login_page.get_email_error_message()
        
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_EMPTY_EMAIL, email_error, "Email error message is not as expected.")
        self.assert_all()

    def test_short_password(self):
        self.login_page.enter_email(VALID_USER_EMAIL)  
        self.login_page.enter_password(SHORT_PASSWORD) # Password with less than 6 characters (boundary value analysis)
        self.login_page.click_loginButton()  
        password_error = self.login_page.get_password_error_message()
        
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_SHORT_PASSWORD, password_error, "Password error message is not as expected.")
        self.assert_all()

    def test_long_password(self):
        self.login_page.enter_email(VALID_USER_EMAIL)  
        self.login_page.enter_password(LONG_PASSWORD)  #Password with more than 15 characters (boundary value analysis)
        self.login_page.click_loginButton() 
        password_error = self.login_page.get_password_error_message()
        
        self.soft_assert(self.assertEqual, ERROR_MESSAGE_LONG_PASSWORD, password_error, "Password error message is not as expected.")
        self.assert_all()

    
    




    



    

        

