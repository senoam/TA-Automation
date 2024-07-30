from .BasePage import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.input_email =  "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextEmail')]"
        self.input_password = "//*[contains(@resource-id, 'textInputEditTextPassword')]"
        self.btn_login = "//*[contains(@class, 'Button') and contains(@resource-id, 'appCompatButtonLogin')]"
        self.btn_create_account = "//*[contains(@class, 'TextView') and contains(@resource-id, 'textViewLinkRegister')]"
        self.txt_failed_login = "//*[contains(@text, 'Wrong Email or Password')]"

    def login(self, email : str, password : str):
        
        self.wait_element(self.btn_login, 4)
        self.send_keys(self.input_email, email, 5)
        self.send_keys(self.input_password, password, 2)
        self.click_element(self.btn_login, 4)



    def tap_create_account(self):
        self.click_element(self.btn_create_account, 1)

    def assert_failed_login(self):
        self.find_element(self.txt_failed_login)

