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

To run the test, run this command

```
pytest api-test/test_api.py -s
```
