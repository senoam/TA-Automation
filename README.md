# TA-Automation

Make sure we are in the project directory.

cd to `api-test` folder

## 1. Automation API Test

To setup a virtual environment in python 3, run this following command:

```
python3 -m venv testenv
```

this will create a virtual environment called `testenv` in the project directory.

After initializing the virtual environment, run this command to start activating the virtual environment:

```
source testenv/bin/activate
```

Inside the environment, run this command to install all the required packages:

```
pip install -r ../requirements.txt
```

To run the test, run this command

```
pytest api-test/test_api.py -s
```

When you are finished running the test, run this command to exit the venv

```
deactivate
```

### Test Cases

1. Test Get API (Check data type and response code)
2. Test Post API (Check data type, content, response code and length)

## 2. Automation Android Test

For this part, you have to cd to the `app-automation` folder

Make sure you have already setup `node` in you machine, since it is needed to install appium. Run this to install Appium

```
npm install -g appium
```

and if you have not set up the PATH for android tools, run this command

```
export PATH=~/Library/Android/sdk/tools:$PATH
export PATH=~/Library/Android/sdk/platform-tools:$PATH
```

```
source ~/.bash_profile
```

After setting up appium, type `appium` in the command line to start appium server.
These are the following variables for the Android Emulator that my machine uses, feel free to change to whatever fits your machine inside the conftest.py

```
    appium_server_url = 'http://127.0.0.1:4723'
    platformName='android',
    platormVersion='7',
    automationName='uiautomator2',
    deviceName='emulator-5554'
```

setup the python venv one more time in the `app-automation` folder and run these commands separately

```
python3 -m venv testenv
source testenv/bin/activate
pip install -r ../requirements.txt
```

To test the app, run

```
pytest test_login.py
```

The test will approximately take 2 minutes until it finishes. In most cases, the test can run perfectly. However, I have found some hiccups in the connectivity of the test suite to the appium server. Please re-run the test if you find such issue.

In this setup, I built a test automation framework (android) that is based on pytest and appium. The setup follows the Page-Object Model Design Pattern, where the test steps are stored in `test_login.py` file in the outer directory. While the object interactions are located inside their respective pages inside `pages` folder.

### Test Cases

Positive:

1. Verify Registration and Success Login

   Expected Result: User is registered and logged in. Data is recorded in the Menu page.

2. Verify If There are More than One Account Registered

   Expected Result: New user data is registered and logged in. Data is recorded in the Menu page with the existing data is still present.

Negative:

1. Verify Invalid Password on Login

   Expected Result: Fail to Login

2. Verify Email not registered on Login

   Expected Result: Fail to Login

3. Verify Empty Email on Login

   Expected Result: Fail to Login

4. Verify Empty fields when Registering

   Expected Result: Fail to Register

5. Verify Email Already Exists when Registering

   Expected Result: Fail to Register
