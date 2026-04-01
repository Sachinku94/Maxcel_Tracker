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

    
    def test_scope_injection(self):
        log= self.getLogger()

        injected_scope_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
        "redirect_uri=https%3A%2F%2Fstg-fe.maxeltracker.com%2Fapi%2Fauth%2Fgoogle%2Fcallback&"
        "response_type=code&"
        "scope=openid%20email%20profile%20https://www.googleapis.com/auth/admin.directory.user&"
        "access_type=offline&"
        "prompt=consent"
    )
        
        self.driver.get(injected_scope_url)
        time.sleep(5)
        current_url = self.driver.current_url
        assert "error" in current_url or "consent" in current_url, "Scope injection test failed"




    def test_redirect_uri_manipulation(self):
        log= self.getLogger()

        tampered_url = (
            "https://accounts.google.com/o/oauth2/v2/auth?"
            "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
            "redirect_uri=https%3A%2F%2Fevil.com%2Fcallback&"
            "response_type=code&"
            "scope=openid%20email%20profile&"
            "access_type=offline&"
            "prompt=consent"
        )

        self.driver.get(tampered_url)
        time.sleep(5)
        current_url = self.driver.current_url
        assert "error" in current_url or "redirect_uri_mismatch" in current_url, "Redirect URI manipulation test failed"

    def test_loginwithgoogle(self):
        log= self.getLogger()
        time.sleep(10)
        logout=By.ID,"sidebarWrapper"
        self.driver.find_element(*logout).click()
        lbutton=By.XPATH,"//span[contains(text(),'Logout')]"
        self.driver.find_element(*lbutton).click()
        time.sleep(20)
        login=By.XPATH,"//span[contains(text(),'Google')]"
        self.driver.find_element(*login).click()
    
    def test_authorization(self): # to  test the autohorization use the specific user account which has limited acces;
        log= self.getLogger()
        time.sleep(10)
        time.sleep(10)
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        app=[HomePage.kpi(self),HomePage.appsandwebsite(self),HomePage.roles(self),HomePage.screen_record(self)]
        user=By.ID,"sidebar-profile-txt"
        user_profile=wait.until(EC.presence_of_element_located(user))
        user_name=user_profile.text
        if user_name=="Akash Sharma":
        
         for ap in app:
            self.driver.get(ap)
            response=requests.get(ap)
            time.sleep(5)
            denied_url=self.driver.current_url
            assert "access-denied" in denied_url or "access_denied" in denied_url, f"Expected access denied but got {denied_url}"
            
        else :
            log.info(f"User {user_name} does not have limited access, skipping authorization test.")
        # status=response.status_code
        # log.info(status)
        # if status == 307 or status == 403:
        #     log.info(f"Authorization test passed: Access is correctly denied with status code {status}")
        # else:
        #     log.error(f"Authorization test failed: Expected status code 403 but got {status}")
        # assert status == 307, f"Expected status code 307 but got {status}"