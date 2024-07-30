from .BasePage import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class MenuPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.txt_title =  "//android.widget.TextView[@text='Android NewLine Learning']"
        self.txt_own_name = "//*[contains(@class, 'LinearLayoutCompat')]//*[contains(@resource-id, 'textViewName')]"
        self.txt_list_email = "//*[contains(@class, 'RecyclerView') and contains(@resource-id, 'recyclerViewUsers')]//*[@text='Email']//following-sibling::*"
        self.txt_list_name = "//*[contains(@class, 'RecyclerView') and contains(@resource-id, 'recyclerViewUsers')]//*[@text='Name']//following-sibling::*"
        self.txt_list_password = "//*[contains(@class, 'RecyclerView') and contains(@resource-id, 'recyclerViewUsers')]//*[@text='Password']//following-sibling::*"

    def verify_header(self, email : str):
        self.wait_element(self.txt_title, 4)
        text = self.get_text(self.txt_own_name, 3)
        assert email == text


    def verify_account_exists(self, name, email, password):
        self.wait_element(self.txt_list_email, 4)
        self.wait_element(self.txt_list_name, 4)
        self.wait_element(self.txt_list_password, 4)

        self.verify_element(self.txt_list_name + "[@text='"+ name +"']", 3)
        self.verify_element(self.txt_list_email + "[@text='"+ email +"']", 3)
        self.verify_element(self.txt_list_password + "[@text='"+ password +"']", 3)
    
