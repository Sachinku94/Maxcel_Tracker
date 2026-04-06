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

class Testone(BaseClass):   #done


    def test_searchaiuser(self): #assertion issue 
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.ai(self)
        self.driver.get(app)
        time.sleep(5)
        
        time.sleep(2)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_1.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        search_user=By.CSS_SELECTOR,".css-19bb58m"
        search_user=wait.until(EC.presence_of_all_elements_located(search_user))
        for _, row in user_data.iterrows():
            flat_data.extend([row['Name'], row['Department']])
            
        for user,value in zip(search_user, flat_data):
            try:
                user.click()
                time.sleep(2)
                options=By.CSS_SELECTOR,".css-fygc7l-option"
                options=wait.until(EC.presence_of_all_elements_located(options))
                for opt in options:
                    log.info(f"clicking on filter option {opt.text}")
                    if opt.text==row['Name'] or opt.text==row['Department']:
                        opt.click()
                        time.sleep(2)
                        break
                    elif opt.text!=value:
                        random_option=random.choice(options)
                        random_option.click()

                        time.sleep(2)
                        break
            except Exception as e:
                log.info(f"Exception occurred: {e}")
                time.sleep(2)
        cal=By.XPATH,"//input[@placeholder='Select Date']"
        cal=wait.until(EC.presence_of_element_located(cal))
        cal.click()
        time.sleep(2)
        filter_days=By.XPATH,"//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li"
        filter_days=wait.until(EC.presence_of_all_elements_located(filter_days))
        n=0
        for i in filter_days:
            if n<5:
                i.click()
                time.sleep(3)
                cal.click()
                n+=1
        tembtn=By.CSS_SELECTOR,".themeBtn"
        tembtn=wait.until(EC.presence_of_element_located(tembtn))
        tembtn.click()
        time.sleep(2)

        tost=By.CSS_SELECTOR,".Toastify__toast-body>div:last-child"
        tost=wait.until(EC.presence_of_element_located(tost))
        log.info(f"Toast message: {tost.text}")
        assert "Report generation started. You'll be notified by email once ready." in tost.text
