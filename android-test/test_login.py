from appium import webdriver
import unittest
from base_test import BaseTest

class TestLogin(BaseTest):
    
    @classmethod
    def setUpClass(cls) -> None:
        super(TestLogin, cls).setUpClass()
        # Do things here that are needed only once (like loging in)

    def setUp(self) -> None:
        # This is executed before every test
        pass

    def testOne(self):
        # Write your tests here
        print("masuk322")
        pass
    

    def tearDown(self) -> None:
        # This is executed after every test
        pass


if __name__ == '__main__':
    # Load the tests from the suite class we created
    test_cases = unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
    # If you want do add more
    # test_cases.addTests(TestSomethingElse)

    # Run the actual tests
    unittest.TextTestRunner().run(test_cases)
