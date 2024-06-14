import pytest
import os
from base.DriverClass import  Driver


@pytest.fixture(scope="function")  # This fixture is responsible for setting up the
#  driver for  tests, and it has session scope.
def session_driver(request):
    driver = Driver.getdrivermethod(Browser='chrome')
    print("Before Session ")
    def session_cleanup():
        driver.quit()

    request.addfinalizer(session_cleanup)  # A finalization function is registered to quit
    # the driver when the entire test session ends.
    return driver  # The driver instance is returned for use in tests.


@pytest.fixture(scope="function")  # This fixture is used to share the same driver
# instance among test classes and has class scope.
def web_driver(request, session_driver):
    driver = session_driver

    if request.cls is not None:
        request.cls.driver = driver

    return driver
