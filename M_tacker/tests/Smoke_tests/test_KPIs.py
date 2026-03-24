from logging import log
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
import random
import pandas as pd
import requests

class Testone(BaseClass):


    def test_kpisearch(self):
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.kpi(self)
        self.driver.get(app)
        time.sleep(5)
        time.sleep(2)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_1.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        filter_but=By.XPATH,"//input[@placeholder='Search by Title or Description']"
        filter_button=wait.until(EC.presence_of_all_elements_located(filter_but))
        for _, row in user_data.iterrows():
            flat_data.extend([ row['Department']])
            for i in filter_button:
                i.click()
                i.send_keys(row['Department'])
                time.sleep(2)
                i.send_keys(Keys.ENTER)
                
                time.sleep(2)
                searcheduser=By.XPATH,"//span[@class='text-[14px] font-semibold text-Custom-Black-700 text-ellipsis whitespace-nowrap overflow-hidden cursor-default capitalize']"
                searcheduser=wait.until(EC.visibility_of_element_located(searcheduser))
                log.info(f"verifying the search item {searcheduser.text}")
                assert searcheduser.text==row['Department'],f"search item {searcheduser.text} is not matching with {row['Department']}"
                i.clear()
        log.info("Department search functionality is working fine")


    def test_kpicreation(self): #need to create a proper data in excel file and crate click is pending in the kpi page
        # .themeBtn
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.kpi(self)
        self.driver.get(app)
        time.sleep(5)
        time.sleep(2)
        create_but=By.CSS_SELECTOR,".themeBtn"
        create_button=wait.until(EC.element_to_be_clickable(create_but))
        create_button.click()
        # .outline-none
        field=By.CSS_SELECTOR,".outline-none"
        field_name=wait.until(EC.presence_of_all_elements_located(field))
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_user.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        for _, row in user_data.iterrows():
            al_opt.extend([row['role'], row['user'], row['department'], row['shift'], row['device']])
        for value, field in zip(al_opt, field_name):
                field.click()
                time.sleep(2)
                field.send_keys(value)
                time.sleep(2)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_user.xlsx") 
        for _, row in user_data.iterrows():
            flat_data.extend(row['role'])      
        send_data=By.CSS_SELECTOR,".css-19bb58m input"
        send_button=wait.until(EC.visibility_of_element_located(send_data))
        for value in zip(flat_data):
            send_button.click()
            time.sleep(3)

            log.info(f"Entering value: {value}")

            send_button.send_keys(value)


            time.sleep(3)

            drop_down = self.driver.find_elements(By.CSS_SELECTOR, ".css-fygc7l-option")
            for option in drop_down:
                if option.text.strip() == value:
                    option.click()
                    log.info(f"Selected value: {value}")
                    break

            time.sleep(2)

    



