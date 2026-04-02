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

class Testone(BaseClass): #pass


    def test_emailradiobtn(self):
        time.sleep(10)
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.alerts(self)
        self.driver.get(app)
        time.sleep(5)
        radio_btn=By.CSS_SELECTOR,".transition-colors"
        radio_btn=wait.until(EC.presence_of_all_elements_located(radio_btn))
        for i in radio_btn:
            i.click()
            time.sleep(2)   
        log.info("All radio buttons are working correctly.")
        drop=By.CSS_SELECTOR,".css-c2frko-control"
        drop=wait.until(EC.presence_of_all_elements_located(drop))
        for i in drop:
            i.click()
            time.sleep(2)
            options=By.CSS_SELECTOR,".css-fygc7l-option"
            options=wait.until(EC.presence_of_all_elements_located(options))
            choice=random.choice(options)
            choice.click()
            time.sleep(2)
        log.info("All dropdown options are working correctly.")
        mintime=By.CSS_SELECTOR,".css-12qyxrh-control"
        mintime=wait.until(EC.presence_of_all_elements_located(mintime))
        for i in mintime:
            i.click()
            time.sleep(2)
            optmin=By.CSS_SELECTOR,".css-1726jq5-option"
            optmin=wait.until(EC.presence_of_all_elements_located(optmin))
            choice=random.choice(optmin)
            choice.click()
            time.sleep(2)
        log.info("All minute options are working correctly.")
        checkbox=By.CSS_SELECTOR,".checkmark"
        checkbox=wait.until(EC.presence_of_all_elements_located(checkbox))
        for i in checkbox:
            i.click()
            time.sleep(2)
        log.info("All checkbox options are working correctly.")