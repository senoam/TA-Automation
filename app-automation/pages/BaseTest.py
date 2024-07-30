import pytest

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    def get_app(self):
        print("App")