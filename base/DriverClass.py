import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# In this class, it contains the basic driver class where the driver is declared.

class Driver:

    @classmethod
    def getdrivermethod(self, Browser='chrome'):
        if (Browser == 'chrome'):
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument(r"--user-data-dir=C:\Users\rethi\AppData\Local\Google\Chrome\User Data")
            # provide the profile name with which we want to open browser
            options.add_argument(r'--profile-directory=Profile 3')
            driver = webdriver.Chrome()
        elif (Browser == 'edge'):
            driver = webdriver.Edge()


        return driver
