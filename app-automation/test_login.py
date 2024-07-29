from pages.BaseTest import BaseTest
from pages.LoginPage import LoginPage
import pytest

class Test_Regression(BaseTest):

    def test_login_failed(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("Test@gmail.com", "test1234")

if __name__ == "__main__":
  pytest.main(["-q","test_login.py"])