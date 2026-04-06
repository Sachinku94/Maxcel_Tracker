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
            
            h4=By.XPATH,"//div/h4"
            heading=wait.until(EC.presence_of_all_elements_located(h4))
            n=0

            for head in  heading:
                
                time.sleep(5)
                btn=By.CSS_SELECTOR,".custom-max-sm-l\:py-\[30px\]"
                return_btn=wait.until(EC.presence_of_all_elements_located(btn))
                return_btn[n].click()
                t=head.text.lower()
                log.info(f"Clicked on settings option: {t}")
                

                time.sleep(10)
                current_url=self.driver.current_url
                
                log.info(f"Current URL after clicking settings: {current_url}")
                assert t in current_url, f"Expected URL to contain '{t}', but got {current_url}"
                breadcrum=By.CSS_SELECTOR,".leading-5"
                breadcrumb=wait.until(EC.presence_of_all_elements_located(breadcrum))
                breadcrumb_text=breadcrumb[1].text.lower()
                log.info(f"Breadcrumb text: {breadcrumb_text}")
                assert breadcrumb_text in current_url, f"Expected URL to contain '{breadcrumb_text}', but got {current_url}"
                self.driver.back()
                log.info("Navigated back to settings page.")
                time.sleep(5)
                self.driver.refresh()
                n+=1
                time.sleep(5)
        except NoSuchElementException:
            log.info("Settings options not found, skipping the test.")