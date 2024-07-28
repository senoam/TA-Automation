from selenium.webdriver.common.by import By
from appium import webdriver


inputEmailField = "//*[contains(@class, 'EditText') and contains(@resource-id, 'textInputEditTextEmail')]"



def insertEmail(email):
    webdriver.WebElement.