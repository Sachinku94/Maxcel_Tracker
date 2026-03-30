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
from selenium.webdriver.common.action_chains import ActionChains as AC
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testone(BaseClass):

    def test_streamsearch(self):
        log=self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        user=HomePage.livestream(self)
        self.driver.get(user)
        time.sleep(5)
        searchusr=By.CSS_SELECTOR,".css-19bb58m"
        users=wait.until(EC.visibility_of_all_elements_located(searchusr))
        if users:
            user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_user.xlsx")
            count=len(user_data)
            log.info(f"Total number of users: {len(user_data)}")
            flat_data = []

            for _, row in user_data.iterrows():
                flat_data.extend([row['department'], row['user']])
            for user,value in zip(users, flat_data):
             try:
                 user.click()
                 time.sleep(2)
                 time.sleep(2)
                 options=self.driver.find_elements(By.CSS_SELECTOR,".css-fygc7l-option")
                 n=0
                 for option in options:
                    log.info(f"clicking on filter option {option.text}")
                    log.info(f"comparing {option.text} with {value}")
                    if option.text==value:
                        log.info(f"Clicking on option: {option.text}")
                        option.click()
                        log.info(f"Selected value: {value}")
                        break
                    
                        
             except NoSuchElementException as e:
                        log.error(f"Element not found: {e}")
             except StaleElementReferenceException as e:
                        log.error(f"Stale element reference: {e}")


    def test_userscountsonlineoffline(self):
        log=self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        user=HomePage.livestream(self)
        self.driver.get(user)
        time.sleep(20)
        # online_offline=By.CSS_SELECTOR,".transition-all"
        # online_offline_users=wait.until(EC.presence_of_all_elements_located(online_offline))
        # for user in online_offline_users:
        #      text=user.text
        #      time.sleep(4)
        #      log.info(f"User status: {text}")
        
        # log.info(f"Number of online/offline users: {len(online_offline_users)}")
        online_users =By.XPATH,"//*[contains(@class, 'ring-green-600')]//p[2]"
        online_users_count=wait.until(EC.presence_of_element_located(online_users))
        log.info(f"Number of online users: {online_users_count.text}")
        allonline_users=By.CSS_SELECTOR,".checkmark"
        all_online_users=wait.until(EC.presence_of_all_elements_located(allonline_users))
        log.info(f"Total online users: {len(all_online_users)}")
        # assert len(all_online_users)==int(online_users_count.text),"Online users count does not match the displayed count"
        time.sleep(5)

        clkoffline_users=By.XPATH,"//*[contains(@class, 'bg-Custom-Light-Red')]"
        clkoffline_users=wait.until(EC.presence_of_element_located(clkoffline_users))
        clkoffline_users.click()
        time.sleep(10)
        offline_users=By.XPATH,"//*[contains(@class, 'ring-red-600')]/p[2]"
        offline_users_count=wait.until(EC.presence_of_element_located(offline_users))
        log.info(f"Number of offline users: {offline_users_count.text}")
        alloffline_users=By.CSS_SELECTOR,".transition"
        all_offline_users=wait.until(EC.presence_of_all_elements_located(alloffline_users))
        log.info(f"Total offline users: {len(all_offline_users)}")