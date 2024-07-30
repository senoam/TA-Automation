from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.input_name = "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextName')]"
        self.input_email = "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextEmail')]"
        self.input_password = "//*[contains(@resource-id, 'textInputEditTextPassword')]"
        self.input_confirm_password = "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextConfirmPassword')]"
        self.btn_register = "//*[contains(@class, 'Button') and contains(@resource-id, 'appCompatButtonRegister')]"
        self.txt_invalid_name = "//*[contains(@text, 'Enter Full Name')]"
        self.txt_invalid_email = "//*[contains(@text, 'Enter Valid Email')]"
        self.txt_email_already_exists = "//*[contains(@text, 'Email Already Exists')]"


    def register(self, name : str, email : str, password : list):

        self.send_keys(self.input_name, name, 10)
        self.send_keys(self.input_email, email, 3)
        self.send_keys(self.input_password, password[0], 3)
        self.send_keys(self.input_confirm_password, password[1], 3)

        self.click_register()

    def tapBack(self):
        # self.driver.press_keycode(4)
        self.back()

    def click_register(self):
        self.driver.swipe(0, 400, 0, 200, 1000)
        self.click_element(self.btn_register, 4)

    def assert_invalid_name(self):
        self.verify_element(self.txt_invalid_name, 4)

    def assert_invalid_email(self):
        self.verify_element(self.txt_invalid_email, 4)
    
    def assert_in_registration_page(self):
        self.verify_element(self.btn_register, 4)
    
    def assert_email_already_exists(self):
        self.verify_element(self.txt_email_already_exists, 4)