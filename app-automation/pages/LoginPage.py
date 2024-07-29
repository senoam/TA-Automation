from .BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    USER_NAME = (By.XPATH, "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextEmail')]")
    PASSWORD = (By.XPATH, "//*[contains(@resource-id, 'textInputEditTextPassword')]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@class, 'Button') and contains(@resource-id, 'appCompatButtonLogin')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.input_user_name = self.find_element(*self.USER_NAME)
        self.input_password = self.find_element(*self.PASSWORD)
        self.button_login = self.find_element(*self.LOGIN_BUTTON)

    def login(self, user_name, password):
        self.input_user_name.clear()
        self.input_user_name.send_keys(user_name)
        self.input_password.clear()
        self.input_password.send_keys(password)
        self.button_login.click()

