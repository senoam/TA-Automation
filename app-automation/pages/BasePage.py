import selenium
from appium.webdriver.common.mobileby import MobileBy
import selenium.common
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        
    def wait_element(self, locator, timeout):
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        element = WebDriverWait(self.driver, timeout,ignored_exceptions=ignored_exceptions)\
                                .until(EC.element_to_be_clickable((MobileBy.XPATH, locator)))
        
    
    def verify_element(self, locator, timeout):
        self.wait_element(self, locator, timeout)
        self.driver.find_element(by=MobileBy.XPATH, value=locator)

    def click_element(self, locator, timeout):
        self.wait_element(locator, timeout)
        self.driver.find_element(by=MobileBy.XPATH, value=locator).click()

    def verify_element(self, locator):
        self.driver.find_element(by=MobileBy.XPATH, value=locator)

    def send_keys(self, locator, content, timeout):
        
        self.wait_element(locator, timeout)
        
        self.driver.find_element(by=MobileBy.XPATH, value=locator).send_keys(content)
        self.driver.hide_keyboard()

    def back(self):
        self.driver.back()