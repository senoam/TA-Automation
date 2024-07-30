import pytest
import pytest
from appium import webdriver
import unittest
from utils.constants import ROOT_DIR
# from appium.webdriver.common.mobileby import mobileby


capabilities = dict(
    platformName='android',
    platormVersion='7',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    language='en',
    app= ROOT_DIR + '/apk/Sample Android App - Login Tes_4.0_APKPure.apk',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723'


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Remote(appium_server_url, capabilities)
    request.cls.driver = driver
    yield