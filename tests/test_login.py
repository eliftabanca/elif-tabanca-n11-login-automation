import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils.config import *
from tests.conftest import *

@pytest.mark.usefixtures("setup")
class TestLogin:
    
     
    def test_valid_login(self, setup):
        login_page = LoginPage(self.driver)
        login_page.open_url(BASE_URL)
        login_page.enter_email(VALID_USER_EMAIL) 
        login_page.enter_password(VALID_USER_PASSWORD)
        login_page.click_login()
        # Assert: User should be redirected to homepage (check for a specific element on homepage)
