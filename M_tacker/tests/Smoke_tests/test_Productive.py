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

    
    def test_appclendar(self):
        
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.productive(self)
        self.driver.get(app)
        cel=By.XPATH,"//input[@placeholder='Select Date']"
        celandar=wait.until(EC.presence_of_element_located(cel))
        celandar.click()
        time.sleep(2)
        filter_days=By.XPATH,"//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li"
        filter_days=wait.until(EC.presence_of_all_elements_located(filter_days))
        for i in filter_days:
            i.click()
            time.sleep(1)
            celandar.click()

    def test_appfilter(self):
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.productive(self)
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
            flat_data.extend([row['shift'], row['department']])
            for i in filter_button:
                i.click()
                time.sleep(2)
                selected_opt=By.CSS_SELECTOR,".css-1n081kd-singleValue"
                selected_opt=wait.until(EC.presence_of_all_elements_located(selected_opt))
                for i in selected_opt:
                    log.info(f"already selected filter option is {i.text}")
                    al_opt.append(i.text)

                
                
                if row['shift'] and row['department'] not in al_opt:
                            log.info(f"clicking on filter option {row['shift']or row['department']}")
                            option_shift_department=By.CSS_SELECTOR,".css-fygc7l-option"
                            option_shift_d=wait.until(EC.visibility_of_all_elements_located(option_shift_department))
                            for e in option_shift_d:
                                if e.text==row['shift'] or e.text==row['department']:
                                    e.click()
                                    break
                al_opt.clear()               
                time.sleep(2)
            # shift filter not responding  
                    
    def test_actionsonapp(self):
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=HomePage.productive(self)
        self.driver.get(app)
        act=By.CSS_SELECTOR,"div.MenuOuterDrop.supertab"  
        action_button=wait.until(EC.presence_of_all_elements_located(act))
        for i in action_button:
             i.click()
             time.sleep(2)
             graphs=By.XPATH,"//div[@class='p-[12px]']/li"   
             graphs_options=wait.until(EC.visibility_of_any_elements_located(graphs))
             for j in graphs_options:
                 log.info(f"clicking on graph option {j.text}")
                 j.click()
                 time.sleep(2)
                 i.click() 
             self.driver.execute_script("window.scrollTo(0,200);")
             time.sleep(2)
             
             
             



                 
             
            
            


        