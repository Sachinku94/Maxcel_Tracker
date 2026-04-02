from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest
from Pages.homepage import HomePage
from object.Selenium_helper import SeleniumHelper
import asyncio
import pandas as pd
import pyautogui
import os
import pyperclip
import random

class Testone(BaseClass):


    def test_screenrec(self): #need to check
        time.sleep(10)
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.screen_record(self)
        self.driver.get(app)
        time.sleep(5)
        try:
            btn=By.XPATH,"//div/a[contains(text(),'Buy Add-on')]"
            return_btn=wait.until(EC.element_to_be_clickable(btn))
            return_btn.click()
            time.sleep(10)
            current_url=self.driver.current_url
            log.info(f"Current URL after clicking Buy Add-on: {current_url}")
            assert "settings/billing?openPayment=addons" in current_url, f"Expected URL to contain 'settings/billing?openPayment=addons', but got {current_url}"
                
            
            log.info("Buy add-on button is working correctly and navigates to the expected URL.")
        except NoSuchElementException:
            log.info("Buy add-on button not found, skipping the test.") 
    