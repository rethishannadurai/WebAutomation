import os
import time
from datetime import timedelta, datetime

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import utilities.CustomLogger as cl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# This class contains all the basic functions that are done while inspecting an Element
'''This class contains the following methods

clickelements
isdisplayed
sendkeys
gettext
screenshot

for All the above mentioned methods, first it will get the element by locatortype & locator value using "getelement"
getelement uses wait for element method to wait for certain time if element not found it will throw an expection and take a screenshot
'''


def convert_date_format(input_date, input_format, output_format):
    date_obj = datetime.strptime(input_date, input_format)
    return date_obj.strftime(output_format)


class BaseFn:
    log = cl.customLogger()

    def __init__(self, driver):  # Here driver is an argument which should be passed when his BaseFn is called.
        # this driver comes from the driverclass
        self.driver = driver

    def waitforElement(self, locatortype, locatorvalue, locatorvalue2=None):
        locatortype.lower()
        element = None

        wait = WebDriverWait(self.driver, 50, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        try:
            if locatortype == "id":
                element = wait.until(lambda x: x.find_element(by=By.ID, value=locatorvalue))
                return element
            elif locatortype == "class":
                element = wait.until(lambda x: x.find_element(by=By.CLASS_NAME, value=locatorvalue))
                return element
            elif locatortype == "name":
                element = wait.until(lambda x: x.find_element(by=By.NAME, value=locatorvalue))
                return element
            # UiSelector().description("23 October 2023")

            elif locatortype == "css":
                element = wait.until(lambda x: x.find_element(by=By.CSS_SELECTOR,
                                                              value=locatorvalue))
                return element
            elif locatortype == "linktext":
                element = wait.until(lambda x: x.find_element(by=By.LINK_TEXT,
                                                              value=locatorvalue))
                return element
            elif locatortype == "partiallinktext":
                element = wait.until(lambda x: x.find_element(by=By.PARTIAL_LINK_TEXT,
                                                              value=locatorvalue))
                return element
            elif locatortype == "tag":
                element = wait.until(lambda x: x.find_element(by=By.TAG_NAME,
                                                              value=locatorvalue))
                return element
            elif locatortype == "xpath":
                element = wait.until(lambda x: x.find_element(by=By.XPATH, value=locatorvalue))
                return element

            else:
                if locatorvalue2 is None:
                    self.log.info("Locator value " + locatorvalue + "not found")
                    self.takescreenshot("Element not found")
                    self.screenShot("Element not found")
                else:
                    self.log.info("Locator value " + locatorvalue + "& LocatorValue2 " + locatorvalue2 + "not found")
                    self.takescreenshot("Element not found")
                    self.screenShot("Element not found")
        except Exception as e:
            self.log.error(f"TimeoutException: {e}")
            error_message = "Element_not_found"
            self.takescreenshot(error_message)
            raise
        return element
    def getElement(self, locatortype, locatorvalue, locatorvalue2=None):
        element = None
        # try:
        locatortype = locatortype.lower()
        element = self.waitforElement(locatortype, locatorvalue, locatorvalue2)
        if locatorvalue2 is None:
            self.log.info("Element found with LocatorType: " + locatortype
                          + " with the locatorvalue :" + locatorvalue)
        else:
            self.log.info("Element found with LocatorType: " + locatortype
                          + " with the locatorvalue1 :" + locatorvalue + " locatorvalue2" + locatorvalue2)
        '''
        except:
            if locatorvalue2 is None:
                self.log.info(
                    "Element not found with LocatorType: " + locatortype
                    + " and with the locatorvalue :" + locatorvalue)
            else:
                self.log.info(
                    "Element not found with LocatorType: " + locatortype
                    + " and with the locatorvalues1 :" + locatorvalue + " locator 2:" + locatorvalue2)

            '''

        return element

    def clickElement(self, locatortype, locatorvalue, locatorvalue2=None):
        element = None
        # try:
        locatortype = locatortype.lower()
        element = self.getElement(locatortype, locatorvalue, locatorvalue2)
        if element is not None:
            element.click()
            if locatorvalue2 is None:
                self.log.info("Element has clicked  with LocatorType: " + locatortype +
                              " and with the locatorvalue :" + locatorvalue)
            else:
                self.log.info("Element has clicked  with LocatorType: " + locatortype +
                              " and with the locatorvalue1" + locatorvalue + " locator 2:" + locatorvalue2)
        else:
            self.log.info("Element  with LocatorType: " + locatortype +
                          " and with the locatorvalue :" + locatorvalue + " is empty")
        if element is None:
            self.log.info("Unable to click the element  with LocatorType: " + locatortype +
                          " and with the locatorvalue :" + locatorvalue)
            self.takescreenshot(locatortype)
            self.screenShot("Element not found" + locatorvalue)
            assert False
    def isdisplayed(self, locatortype, locatorvalue):
        # try:
        locatortype = locatortype.lower()
        try:
            element = self.getElement(locatortype, locatorvalue)
            if element is not None:
                # element.is_displayed()
                self.log.info(
                    " Element with LocatorType: " + locatortype + " and with the locatorvalue :" + locatorvalue + "is displayed ")
                return True
            else:
                self.log.info("Element  with LocatorType: " + locatortype +
                              " and with the locatorvalue :" + locatorvalue + " is empty")
                return False
        except:
            return False
    def sendkeys(self, text, locatortype, locatorvalue):
        element = None
        # try:
        locatortype = locatortype.lower()
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            element.send_keys(text)
            self.log.info(text + "Text has been successfully entered in the element with LocatorType: "
                          + locatortype + " and with the locatorvalue :" + locatorvalue)
        else:
            self.log.info("Element  with LocatorType: " + locatortype +
                          " and with the locatorvalue :" + locatorvalue + " is empty")

        '''except:
            self.log.info("Unable to enter text  with LocatorType: " + locatortype
                          + " and with the locatorvalue :" + locatorvalue)
            self.takescreenshot(locatortype)
            assert False
        '''


    def gettext(self, textfield, locatortype, locatorvalue, locatorvalue2=None):
        element = self.getElement(locatortype, locatorvalue, locatorvalue2)
        if element is not None:
            text = element.text
            self.log.info("Printing in textfield " + textfield + " : " + text + "")
            cl.allureLogs("Printing in textfield " + textfield + " : " + text + "")
            return text
        else:
            self.log.info("Element  with LocatorType: " + locatortype +
                          " and with the locatorvalue :" + locatorvalue + " is empty")
    def screenShot(self, screenshotname):
        screenshots_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'screenshots')
        current_time = time.strftime("%d_%m_%y_%H_%M_%S")
        filename = f"{screenshotname}_{current_time}.png"
        screenshotpath = os.path.join(screenshots_directory, filename)
        try:
            self.driver.save_screenshot(screenshotpath)
            self.log.info("Screenshot has been saved in the location: " + screenshotpath)
        except Exception as e:
            self.log.error("Unable to save the screenshot: " + str(e))
    def takescreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def devicedate(self):
        text = self.driver.get_device_time("YYYY-MM-DD")
        return text

    def calendarpreviousdateselection(self, device_date, focused_date_on_calendar):
        # Convert device date to "Thu, 2 Nov" format
        self.log.info("Before formatting device date:" + device_date)
        self.log.info("before formatting focused_date_on_calendar:" + focused_date_on_calendar)
        formatted_device_date = convert_date_format(device_date, "%Y-%m-%d", "%a, %d %b")
        self.log.info("formatted_device_date" + formatted_device_date)

        focused_day = focused_date_on_calendar.split(", ")[1].split()[0]

        # Check if the focused date matches the device date
        if focused_day in formatted_device_date:
            self.log.info("formatted_device_date & focused_date-on_calendar are equal")
            # Calculate the previous day from the device date
            previous_day = (datetime.strptime(device_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
            # Convert previous day to "Thu, 3 Nov" format
            previous_day_formatted = convert_date_format(previous_day, "%Y-%m-%d", "%d %B %Y")
            self.log.info("previous_day_formatted" + previous_day_formatted)
            return previous_day_formatted
        else:
            self.log.info("coming to else part")
            return None  # Return None if focused date does not match the device date

    def calendarcurrentdateselection(self, device_date):
        # Convert device date to "Thu, 2 Nov" format
        # formatted_device_date = convert_date_format(device_date, "%Y-%m-%d", "%d %B %Y")
        try:
            formatted_device_date = convert_date_format(device_date, "%Y-%m-%d", "%A, %d/%B/%Y")

            self.log.info("calendarcurrentdateselection-->formatted_device_date")
            return formatted_device_date
        except:
            self.log.info("Error in Date format")

    def clearInput(self, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            element.clear()
            self.log.info("Cleared input field with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue)
        else:
            self.log.info(
                "Element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " is empty")

    def selectOptionByText(self, text, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            Select(element).select_by_visible_text(text)
            self.log.info(
                "Selected option by text: " + text + " in dropdown with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue)
        else:
            self.log.info(
                "Dropdown with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " is empty")

    def acceptAlert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.log.info("Accepted the alert")
        except:
            self.log.info("No alert present")

    def dismissAlert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            self.log.info("Dismissed the alert")
        except:
            self.log.info("No alert present")

    def switchToFrame(self, frame_locator_type, frame_locator_value):
        try:
            frame_element = self.getElement(frame_locator_type, frame_locator_value)
            self.driver.switch_to.frame(frame_element)
            self.log.info(
                "Switched to frame with LocatorType: " + frame_locator_type + " and LocatorValue: " + frame_locator_value)
        except:
            self.log.error(
                "Failed to switch to frame with LocatorType: " + frame_locator_type + " and LocatorValue: " + frame_locator_value)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()
        self.log.info("Switched back to default content")

    def checkCheckbox(self, locatortype, locatorvalue):
        checkbox = self.getElement(locatortype, locatorvalue)
        if checkbox is not None:
            if not checkbox.is_selected():
                checkbox.click()
                self.log.info(
                    "Checkbox with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " checked.")
            else:
                self.log.info(
                    "Checkbox with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " already checked.")
        else:
            self.log.info(
                "Checkbox with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")

    def isCheckboxSelected(self, locatortype, locatorvalue):
        checkbox = self.getElement(locatortype, locatorvalue)
        if checkbox is not None:
            return checkbox.is_selected()
        else:
            self.log.info(
                "Checkbox with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")
            return False

    def isRadioButtonSelected(self, locatortype, locatorvalue):
        radio_button = self.getElement(locatortype, locatorvalue)
        if radio_button is not None:
            return radio_button.is_selected()
        else:
            self.log.info(
                "Radio button with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")
            return False

    def hoverOverElement(self, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            ActionChains(self.driver).move_to_element(element).perform()
            self.log.info(
                "Hovered over element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue)
        else:
            self.log.info(
                "Element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")

    def scrollToElement(self, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info("Scrolled to element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue)
        else:
            self.log.info(
                "Element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")

    def switchToWindow(self, window_handle):
        self.driver.switch_to.window(window_handle)
        self.log.info("Switched to window with handle: " + window_handle)

    def getAllWindowHandles(self):
        return self.driver.window_handles


    def scrollPage(self, direction="down", pixels=100):
        if direction.lower() == "down":
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        elif direction.lower() == "up":
            self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
        else:
            self.log.error("Invalid scroll direction. Use 'up' or 'down'.")

    def goBack(self):
        self.driver.back()
        self.log.info("Navigated back to previous page.")

    def goForward(self):
        self.driver.forward()
        self.log.info("Navigated forward to next page.")

    def getCurrentURL(self):
        return self.driver.current_url

    def maximizeWindow(self):
        self.driver.maximize_window()
        self.log.info("Window maximized.")

    def minimizeWindow(self):
        self.driver.minimize_window()
        self.log.info("Window minimized.")

    def getAlertDialogText(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            self.log.info("No alert present.")
            return None

    def isElementEnabled(self, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            return element.is_enabled()
        else:
            self.log.info(
                "Element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")
            return False

    def isElementSelected(self, locatortype, locatorvalue):
        element = self.getElement(locatortype, locatorvalue)
        if element is not None:
            return element.is_selected()
        else:
            self.log.info(
                "Element with LocatorType: " + locatortype + " and LocatorValue: " + locatorvalue + " not found.")
            return False

    def navigateToURL(self, url):
        self.driver.get(url)
        self.log.info("Navigated to URL: " + url)

    def refreshPage(self):
        self.driver.refresh()
        self.log.info("Page refreshed.")

    def getPageTitle(self):
        return self.driver.title
    def pressEnter(self):
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.log.info("Pressed the Enter key.")