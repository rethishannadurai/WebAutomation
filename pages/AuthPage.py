import os
import time

import utilities.CustomLogger as cl
from base.BaseFn import BaseFn
''' In this class, All the locators and the methods are declared '''


class AuthPage(BaseFn):

    def __init__(self, driver):  # this will be executed for all the functions inside this class
        super().__init__(driver)  # Here it calls the basefn class init method
        # As baseclass is already extended from driverclass .
        # So for this page it has to inherit from the basecls
        # driverclass to basefn then this class -----this how driver flow
        self.driver = driver

    # locators in Auth Page


    _createAccount_BTn="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button/span" #id
    _personal="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]"
    _First_Name="firstName" #id
    _Last_Name="lastName" #id
    _Page1_next_Btn="VfPpkd-vQzf8d" #class
    _first_Name_value="test"
    _last_Name_value="test"
    _Calendar_month="gNnnTd" #class
    _Calendar_month_option ="February" #option
    _Calendar_day="day" #id
    _Calendar_year="year" #id

    _gender="gender" #id
    _gender_option="Male" #option and also value =1


    _Page2_next_Btn="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span" #class

    _username="Username" #name

    _username_value="rethishtest2"
    _Page3_next_Btn="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span"



    _password="Passwd" #name
    _password_value="Hello@12345"
    _confirmPassword="PasswdAgain" #name

    _Page4_next_Btn="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span"


    _phNumber="phoneNumberId" #class
    _phNumber_value="7092997795"
    _Page5_next_Btn="/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/span"#phnumber

    _Page6_next_Btn="/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/span" #code page


    _skip_BTN="/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/button/span"

    _Page8_next_Btn="/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/span"

    _TC_Agree="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span"
    def Verify_url(self):
        self.driver.get('https://accounts.google.com/v3/signin/identifier?continue=https://mail.google.com/mail/&service=mail&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        self.takescreenshot("URL launched")
    def Enter_firstandlastname(self):

        self.clickElement("xpath",self._createAccount_BTn)
        time.sleep(5)
        self.clickElement("xpath",self._personal)

        time.sleep(5)
        self.sendkeys(self._first_Name_value,"id",locatorvalue=self._First_Name)
        self.sendkeys(self._last_Name_value,"id",locatorvalue=self._Last_Name)
        self.takescreenshot("first Name and last name are entered")
        self.clickElement("class",self._Page1_next_Btn)

        time.sleep(10)
        self.selectOptionByText(self._Calendar_month_option,locatortype="class",locatorvalue=self._Calendar_month)
        self.sendkeys("01","id",locatorvalue=self._Calendar_day)
        self.sendkeys("2002","id",locatorvalue=self._Calendar_year)
        self.selectOptionByText(self._gender_option,locatortype="id",locatorvalue=self._gender)
        self.takescreenshot("DOB & Gender are entered")
        self.clickElement("xpath",self._Page2_next_Btn)
        time.sleep(10)

        self.sendkeys(self._username_value,"name",locatorvalue=self._username)
        self.takescreenshot("username is entered")
        self.clickElement("xpath",self._Page3_next_Btn)


        time.sleep(10)
        self.sendkeys(self._password_value,"name",self._password)
        self.sendkeys(self._password_value,"name",self._confirmPassword)
        self.takescreenshot("PWD is entered")

        self.clickElement("xpath",self._Page4_next_Btn)
        time.sleep(10)


        self.sendkeys(self._phNumber_value,"id",self._phNumber)
        self.takescreenshot("Phone number is entered")

        self.clickElement("xpath",self._Page5_next_Btn)
        time.sleep(15)

        self.takescreenshot("code is entered")
        self.clickElement("xpath",self._Page6_next_Btn)

        self.takescreenshot("Add recovery email page")

        time.sleep(10)
        self.takescreenshot("Add recovery email page")
        self.clickElement("xpath",self._skip_BTN)
        time.sleep(10)
        self.takescreenshot("Review  page")

        self.clickElement("xpath",self._Page8_next_Btn) # review page
        time.sleep(10)
        self.takescreenshot("T& C  page")
        self.clickElement("xpath",self._TC_Agree) # review page
        self.takescreenshot("final")


        time.sleep(10)
