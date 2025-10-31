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

class Testone(BaseClass):

  
    def test_screensshotclendar(self):
        
       
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.screen_shot(self)
        self.driver.get(app)
        cel=By.XPATH,"//input[@placeholder='Select Date Range']"
        celandar=wait.until(EC.presence_of_element_located(cel))
        celandar.click()
        time.sleep(2)
        filter_days=By.XPATH,"//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li"
        filter_days=wait.until(EC.presence_of_all_elements_located(filter_days))
        for i in filter_days:
            i.click()
            time.sleep(3)
            celandar.click()
    

    def test_screenshotfilter(self):
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.screen_shot(self)
        self.driver.get(app)
        time.sleep(5)
        
        time.sleep(2)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        filter_but=By.CSS_SELECTOR,".css-c2frko-control"
        filter_button=wait.until(EC.presence_of_all_elements_located(filter_but))
        for _, row in user_data.iterrows():
            flat_data.extend([row['shift'], row['name']])
            for i in filter_button:
                i.click() 
                try:
                    i.send_keys(row['name'])
                except Exception as e:
                    log.info(f"Exception occurred: {e}")
                    time.sleep(2)
                try:
                    options=By.CSS_SELECTOR,".css-fygc7l-option"
                    options=wait.until(EC.presence_of_all_elements_located(options))
                    for opt in options:
                        log.info(f"clicking on filter option {opt.text}")
                        if opt.text==row['name'] or opt.text==row['shift']:
                            opt.click()
                            time.sleep(2)
                            break
                except Exception as e:
                    log.info(f"Exception occurred while selecting option: {e}")
             #.css-f1pr1s-menu