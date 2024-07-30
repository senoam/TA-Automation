from pages.BaseTest import BaseTest
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.MenuPage import MenuPage
import pytest


name = "John"
email = "johndoe@gmail.com"
password = ["test1234", "test1234"]

class Test_Suite(BaseTest):

    @pytest.mark.order(1)
    def test_register_login_success(self):
        loginPage = LoginPage(self.driver)
        loginPage.tap_create_account()
        
        registerPage = RegisterPage(self.driver)
        registerPage.register(name, email, password)
        self.driver.back()


        loginPage.login(email, password[0])

        menuPage = MenuPage(self.driver)
        menuPage.verify_header(email)
        menuPage.verify_account_exists(name, email, password[0])

        self.driver.back()
    
    @pytest.mark.order(2)
    def test_invalid_password(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("johndoe@gmail.com", "invalid1")
        loginPage.assert_failed_login()

    @pytest.mark.order(3)
    def test_email_not_exist(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("invalid@gmail.com", "test1234")
        loginPage.assert_failed_login()

    @pytest.mark.order(4)
    def test_login_empty_email(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("", "test1234")
        loginPage.assert_invalid_email_format()

    @pytest.mark.order(5)
    def test_register_empty_field_validation(self):
        loginPage = LoginPage(self.driver)
        loginPage.tap_create_account()

        registerPage = RegisterPage(self.driver)

        # The function calls below will not register the user, since all the inputs are invalid
        # Assert All field empty
        registerPage.register("", "", ["", ""])
        registerPage.assert_invalid_name()

        # Assert only name filled
        registerPage.register("Jane", "", ["", ""])
        registerPage.assert_invalid_email()

        # Assert only name and email filled
        registerPage.register("Jane", "jane3@gmail.com", ["", ""])
        registerPage.assert_in_registration_page()

        # Assert only name, email and password filled
        registerPage.register("Jane", "jane3@gmail.com", ["testPass1", ""])
        registerPage.assert_in_registration_page()

        # Assert password mismatch filled
        registerPage.register("Jane", "jane3@gmail.com", ["testPass1", "wrongPass"])
        registerPage.assert_in_registration_page()

        self.driver.back()
    
    @pytest.mark.order(6)
    def test_register_email_already_exists(self):
        loginPage = LoginPage(self.driver)
        loginPage.tap_create_account()

        registerPage = RegisterPage(self.driver)

        # Using the same value as the first test case
        registerPage.register(name, email, password)
        registerPage.assert_email_already_exists()

        self.driver.back()

    @pytest.mark.order(7)
    def test_register_add_account(self):
        loginPage = LoginPage(self.driver)
        loginPage.tap_create_account()

        registerPage = RegisterPage(self.driver)

        secondName = "Aegon the Second"
        secondEmail = "aegon2@gmail.com"
        secondPassword = ["kingslanding", "kingslanding"]
        registerPage.register("Aegon the Second", "aegon2@gmail.com", secondPassword)

        self.driver.back()

        loginPage.login(secondEmail, secondPassword[0])

        menuPage = MenuPage(self.driver)

        # Verify newly registered account is in the database
        menuPage.verify_header(secondEmail)
        menuPage.verify_account_exists(secondName, secondEmail, secondPassword[0])

        # Verify the first account is still in the database (not missing)
        menuPage.verify_account_exists(name, email, password[0])
       
if __name__ == "__main__":
  pytest.main(["-q","test_login.py"])