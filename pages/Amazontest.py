import os
import time

import utilities.CustomLogger as cl
from base.BaseFn import BaseFn


class Amazontest(BaseFn):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators in AmazonPage

    _sign_in ="/html/body/div[1]/header/div/div[3]/div[13]/div[2]/a"
    _emailid="ap_email" #id
    _emailid_value="xxxx"
    _password="ap_password" #id
    _password_value="Developer@123"
    _continue_btn="continue" #id

    _submit_btn="signInSubmit" #id


    _searchBar="twotabsearchtextbox" #id
    _searchtext="Qifutan Car Phone Holder Mount"
    _searchButton="nav-search-submit-button" #id

    _phoneholdername="Qifutan Phone Mount"

    _phoneholder="/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a"

    _addtocart="/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[37]/div[1]/span/span/span/input"
    _addtoCart="submit.add-to-cart" #id

    _fridge="Godrej 223 L 2 Star Nano Shield Technology"
    _AC="LG 1 Ton 4 Star DUAL Inverter Split AC (Copper, AI Convertible 6-in-1 Cooling, 4 Way Swing"


    _goTocart="/html/body/div[1]/div[1]/div/div[1]/div[2]/div/form/span/span/span/input"
    _proceedtobuy="/html/body/div[1]/div[1]/div[4]/div[5]/div/div[1]/div[1]/div/form/div/div[1]/span/span/span/input"

    _creditordebit="/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[6]/div/div[3]/div/div[2]/div/div/div[2]/div/form/div/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/span"
    _entercarddetails="pp-f66msR-405" #id
    _cardnumber="pp-W8bWLj-16"
    _cardnumber_value="5555 5555 5555 4444"
    _expiryyear="/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[3]/div[2]/div[1]/span[3]/span/span/span"
    _expiryyearvalue="pp-W8bWLj-21_9" #id
    _Entercarddetailsbtn="css=input.a-button-input"

    _cvv="pp-HSsRyK-418" #id
    _cvv_value=123
    #then enter key
    _continue_without_save="/html/body/div[8]/div/div/div/div/div/span[1]/span/input"





    def Verify_url(self):
        self.maximizeWindow()

        self.driver.get('https://www.amazon.in')
        self.takescreenshot("URL launched")

    def login(self):
        self.clickElement("xpath",self._sign_in)
        self.sendkeys(self._emailid_value,"id",self._emailid)
        time.sleep(2)
        self.takescreenshot("Entered the email ID")
        self.pressEnter()
        cl.allureLogs("Entered the email ID")
        self.sendkeys(self._password_value,"id",self._password)
        time.sleep(2)
        self.takescreenshot("entered the PWD")
        self.pressEnter()
        cl.allureLogs("entered the PWD")
        time.sleep(5)

        self.pressEnter()
        self.takescreenshot("logged in")

        cl.allureLogs("logged in")

        self.clearInput("id",self._searchBar)

        time.sleep(1)
        self.sendkeys(self._searchtext,"id",self._searchBar)


        time.sleep(1)
        self.clickElement("id",self._searchButton)
        time.sleep(2)
        self.takescreenshot("searched the product")
        self.scrollPage("down", 1000)
        time.sleep(2)
        self.takescreenshot("product found")

        page1Title=self.driver.title.title()

        self.clickElement("xpath",self._phoneholder)
        time.sleep(2)

        self.switchToWindow(self.driver.window_handles[1])
        time.sleep(2)
        self.takescreenshot("Adding to cart")

        self.clickElement("xpath",self._addtocart)
        time.sleep(2)
        self.takescreenshot("Added to cart")

        #self.clickElement("xpath",self._goTocart)
        #time.sleep(2)

      #  self.clickElement("xpath",self._proceedtobuy)
