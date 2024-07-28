# TA-Automation

Make sure we are in the project directory.

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
pip install -r requirements.txt
```

## 1. Automation API Test

To run the test, run this command

```
pytest api-test/test_api.py -s
```

When you are finished running the test, run this command to exit the venv

```
deactivate
```

## 2. Automation Android Test

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
