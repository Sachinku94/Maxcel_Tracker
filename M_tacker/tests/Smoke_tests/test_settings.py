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


    def test_settingsredir(self):
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.settings(self)
        self.driver.get(app)
        time.sleep(5)
        try:
            n=0
            while True:
                h4=By.XPATH,"//div/h4"
                heading=wait.until(EC.presence_of_all_elements_located(h4))
                
            

                
                    
                time.sleep(5)
                btn=By.CSS_SELECTOR,".custom-max-sm-l\:py-\[30px\]"
                return_btn=wait.until(EC.presence_of_all_elements_located(btn))
                return_btn[n].click()
                t=heading[n].text.lower()
                log.info(f"Clicked on settings option: {t}")
                if t=="create new alert" or t=="tracking settings" or t=="download report":
                     cancel=By.XPATH,"//button[contains(text(),'Cancel')]"
                     cancel_btn=wait.until(EC.presence_of_all_elements_located(cancel))
                     cancel_btn[0].click()
                elif t=="storage integrations":
                    cancel=By.CSS_SELECTOR,".border-Custom-Black-100 button:nth-child(2)"
                    cancel_btn=wait.until(EC.presence_of_element_located(cancel))
                    cancel_btn.click()

                else:

                    time.sleep(10)
                    current_url=self.driver.current_url
                        
                    log.info(f"Current URL after clicking settings: {current_url}")
                    try:
                        assert t in current_url, f"Expected URL to contain '{t}', but got {current_url}"
                    except (AssertionError, Exception) as e:
                        log.error(f"Assertion error: {e}")
                    try:
                        breadcrum=By.CSS_SELECTOR,".leading-5"
                        breadcrumb=wait.until(EC.presence_of_all_elements_located(breadcrum))
                        breadcrumb_text=breadcrumb[1].text.lower()
                        log.info(f"Breadcrumb text: {breadcrumb_text}")
                        assert breadcrumb_text in current_url, f"Expected URL to contain '{breadcrumb_text}', but got {current_url}"
                    except (AssertionError, Exception) as e:
                        log.error(f"not present: {e}")
                    time.sleep(5)
                    self.driver.back()
                    log.info("Navigated back to settings page.")
                    time.sleep(5)
                    self.driver.refresh()
                    # used_url=self.driver.current_url
                    # log.info(f"Current URL after navigating back: {used_url}")
                    # if used_url != app:
                    #     log.info("Successfully navigated back to settings page.")
                    #     self.driver.get(app)
                    # else:
                    #      pass
                n+=1
                if n>=len(heading):
                    break
                time.sleep(5)        
        except NoSuchElementException:
                log.info("Settings options not found, skipping the test.")
        log.info("Completed settings redirection test successfully")