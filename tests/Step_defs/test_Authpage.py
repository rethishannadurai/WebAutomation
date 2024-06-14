import time
import allure
from pytest_bdd import *
from pytest_bdd import parsers

import utilities.CustomLogger as cl
from pages.AuthPage import AuthPage
from pages.Amazontest import Amazontest

@scenario("login.feature", "Validate amazon Order", features_base_dir='tests/features')
def test_AppLogin():
    pass

@given("Url is launched")
def url_is_launched(web_driver):
    Amazon_test = Amazontest(web_driver)
    Amazon_test.Verify_url()
    cl.allureLogs("Launched The URL")
    Amazon_test.login()
    cl.allureLogs("searched The order")

