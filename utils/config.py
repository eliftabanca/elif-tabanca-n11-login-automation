from selenium.webdriver.common.by import By

BASE_URL = "https://www.n11.com/giris-yap" 

# Test user credentials
VALID_USER_EMAIL = "validusertest01@gmail.com" 
VALID_USER_PASSWORD = "Password123"  
INVALID_USER_EMAIL = "invaliduser@gmail.com"  
INVALID_USER_PASSWORD = "Wrong123"  

# Facebook user credentials 
FACEBOOK_USER_EMAIL = "validusertest01@gmail.com"  
FACEBOOK_USER_PASSWORD = "validuser123"  

# Invalid password scenarios based on Boundary Value Analysis (BVA)
SHORT_PASSWORD = "12345"  # Password with less than 6 characters (boundary value analysis)
LONG_PASSWORD = "TooLongPassword1"  # Password with more than 15 characters (boundary value analysis)

EMPTY_STRING = ""  

 # Locators
EMAIL_INPUT = (By.ID, "email")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "loginButton") 
ERROR_MESSAGE_INVALID_CREDENTIALS_LOCATOR = (By.CLASS_NAME, "errorText")
ERROR_MESSAGE_EMPTY_EMAIL_LOCATOR = (By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div[2]/div")
ERROR_MESSAGE_EMPTY_EMAIL_LOCATOR = (By.CLASS_NAME, "errorText")
ERROR_MESSAGE_SHORT_PASSWORD_LOCATOR = (By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div[2]/div")
ERROR_MESSAGE_LONG_PASSWORD_LOCATOR = (By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div[2]/div")
# Error messages
ERROR_MESSAGE_INVALID_CREDENTIALS = "E-posta adresi veya şifre hatalı, kontrol edebilir misin?" 
ERROR_MESSAGE_EMPTY_EMAIL = "Geçerli bir e-posta adresi girmelisin."  
ERROR_MESSAGE_EMPTY_EMAIL = "Şifreni girebilir misin?"
ERROR_MESSAGE_SHORT_PASSWORD = "Girilen değer en az 6 karakter olmalıdır."  
ERROR_MESSAGE_LONG_PASSWORD = "Girilen değer en fazla 15 karakter olmalıdır."  


