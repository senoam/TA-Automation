from pages.BaseTest import BaseTest
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.MenuPage import MenuPage
import pytest

class Test_Suite(BaseTest):

    # @pytest.mark.order(1)
    # def test_login_failed(self):
    #     loginPage = LoginPage(self.driver)
    #     loginPage.login("Test@gmail.com", "test1234")

    @pytest.mark.order(1)
    def test_register_success(self):
        loginPage = LoginPage(self.driver)
        loginPage.tap_create_account()

        name = "John"
        email = "johndoe@gmail.com"
        password = ["test1234", "test1234"]
        
        registerPage = RegisterPage(self.driver)
        registerPage.register(name, email, password)
        registerPage.back()

        loginPage.login(email, password[0])

        menuPage = MenuPage(self.driver)
        menuPage.verify_header(email)
        menuPage.verify_account_exists(name, email, password[0])

       
if __name__ == "__main__":
  pytest.main(["-q","test_login.py"])