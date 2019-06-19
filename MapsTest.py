# -*- coding: utf-8 -*-
"""
    Simple iOS testing, showcasing the testings of Maps Application. The below usecases are demonstrated in the Application
    Verifying the Valid and Invalid Address in the Maps
    Validating the various icons and there clickable features on Launch page
    Verifying Map Settings and Maps Issues

    """
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class MapsTests(unittest.TestCase):

    def setUp(self):
        app = "com.apple.Maps"
        self.driver = webdriver.Remote(
                                       command_executor= "http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities={
                                       "app": app,
                                       "platformName": "iOS",
                                       "platformVersion": "12.2",
                                       "deviceName": "iPhone 8",
                                       "connectHardwareKeyboard": False
                                       })

    def tearDown(self):
        sleep(3) #Delay added for demo purpose
        self.driver.terminate_app('com.apple.Maps')

    def find_the_element_click(self, ele_text):
        element = self.driver.find_element_by_accessibility_id(ele_text)
        if (element.is_enabled()):
            element.click()
        else:
            self.assertFalse(element, 'Not Found')

    def find_the_elementpath_click(self, ele_text):
        element = self.driver.find_element_by_xpath(ele_text)
        if (element.is_enabled()):
            element.click()
        else:
            self.assertFalse(element, 'Not Found')

    def assert_if_element_found(self, ele_text):
        element = self.driver.find_element_by_accessibility_id(ele_text)
        if (element.is_enabled()):
            self.assertTrue(element, 'Found')
        else:
            self.assertFalse(element, 'Not Found')

    def find_the_element_sendkeys(self, ele_text, keys):
        self.driver.find_element_by_accessibility_id(ele_text).send_keys(keys)


    def test_search_valid_address(self):
        self.find_the_element_sendkeys('Search for a place or address','1055 escalon avenue')
        sleep(2)#Added for demo purpose
        self.find_the_element_click('1055 Escalon Ave')
        self.assertTrue('Found')

    def test_search_invalid_address(self):
       self.find_the_element_sendkeys('Search for a place or address','@#$%^')
       sleep(2)#Added for demo purpose
       self.assert_if_element_found('No suggestions found.')


    def test_verify_travelicon(self):
        self.find_the_element_click("Search for a place or address")
        self.assert_if_element_found("Travel")

    def test_verify_transporticon(self):
        self.find_the_element_click("Search for a place or address")
        self.assert_if_element_found("Transport")

    def test_verify_healthicon(self):
        self.find_the_element_click("Search for a place or address")
        self.assert_if_element_found("Health")

    def test_valid_direction(self):
        self.find_the_element_sendkeys('Search for a place or address','1055 escalon avenue')
        sleep(2)#Added for demo purpose
        self.find_the_element_click('1055 Escalon Ave')
        self.find_the_elementpath_click("//XCUIElementTypeButton[contains(@name,'Directions')]")
        self.find_the_elementpath_click("//XCUIElementTypeButton[@name=\"GO\"]")
        self.find_the_element_click("End")
        self.assertTrue('Valid')

    def test_invalid_direction(self):
        self.find_the_element_sendkeys('Search for a place or address','Bengaluru India')
        sleep(2)#Added for demo purpose
        self.find_the_element_click('Bengaluru, Karnataka, India')
        self.find_the_elementpath_click("//XCUIElementTypeButton[contains(@name,'Directions')]")
        sleep(3)
        self.assert_if_element_found("Directions are not available between these locations.")

    def test_verify_mapSettings(self):
        self.find_the_element_click('Settings')
        self.assert_if_element_found('Maps Settings')

    def test_verify_reportSettings(self):
        self.find_the_element_click('Settings')
        self.find_the_element_click('Report an Issue')
        self.assert_if_element_found('Map Labels')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MapsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
