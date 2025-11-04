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

