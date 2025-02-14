from selenium.webdriver.common.by import By

BASE_URL = "https://www.n11.com/giris-yap" 
HTTP_URL = "http://www.n11.com/giris-yap"   
# Test user credentials
VALID_USER_EMAIL = "t8778925@gmail.com" #"validusertest01@gmail.com" this email was banned by n11.com
VALID_USER_PASSWORD = "test123" #"Password123" this password was banned by n11.com
INVALID_USER_EMAIL = "invaliduser@gmail.com"  
INVALID_USER_PASSWORD = "Wrong123"  


# Invalid password scenarios based on Boundary Value Analysis (BVA)
SHORT_PASSWORD = "12345"  #Password with less than 6 characters (boundary value analysis)
LONG_PASSWORD = "TooLongPassword1"  #Password with more than 15 characters (boundary value analysis)


 #Locators
EMAIL_INPUT = (By.ID, "email")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON_LOCATOR = (By.ID, "loginButton") 
ERROR_MESSAGE_INVALID_CREDENTIALS_LOCATOR = (By.CLASS_NAME, "error-message") #TC3
ERROR_MESSAGE_EMPTY_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#loginForm > div.form-inputs > div:nth-child(1) > div > div")
ERROR_MESSAGE_EMPTY_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#loginForm > div.form-inputs > div:nth-child(2) > div.errorMessage > div")
ERROR_MESSAGE_SHORT_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#loginForm > div.form-inputs > div:nth-child(2) > div.errorMessage > div")
ERROR_MESSAGE_LONG_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#loginForm > div.form-inputs > div:nth-child(2) > div.errorMessage > div")
NOTIFICATION_ACCEPT_BUTTON = (By.CLASS_NAME, "dn-slide-accept-btn")
COOKIE_ACCEPT_BUTTON =   (By.CLASS_NAME, "px-16px py-8px cursor-pointer rounded-4px bg-[#5D3EBC] text-center font-600 text-white")

#Error messages
ERROR_MESSAGE_INVALID_CREDENTIALS = "E-posta adresi veya şifre hatalı, kontrol edebilir misin?" 
ERROR_MESSAGE_EMPTY_EMAIL = "Geçerli bir e-posta adresi girmelisin."  
ERROR_MESSAGE_EMPTY_PASSWORD = "Şifreni girebilir misin?"
ERROR_MESSAGE_SHORT_PASSWORD = "Girilen değer en az 6 karakter olmalıdır."  
ERROR_MESSAGE_LONG_PASSWORD = "Girilen değer en fazla 15 karakter olmalıdır."  

#Asserations
LOGO_LOCATOR = (By.CLASS_NAME, "user")
LOGO_TITLE_TEXT = "t"


