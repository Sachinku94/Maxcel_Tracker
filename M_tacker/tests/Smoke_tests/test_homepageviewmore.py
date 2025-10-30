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

class Testone(BaseClass):

    def test_HomePage(self):
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        cel=By.XPATH,"//input[@placeholder='Select Date Range']"
        celandar=wait.until(EC.presence_of_element_located(cel))
        celandar.click()
        time.sleep(2)
        filter_days=By.XPATH,"//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li"
        filter_days=wait.until(EC.presence_of_all_elements_located(filter_days))
        for i in filter_days:
            i.click()
            time.sleep(1)
            celandar.click()
            
        time.sleep(3)
    def test_dashboardsearch(self):
        item_chossen=[]
        item_choosed=[]
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        searchbox=By.XPATH,"(//div[@class='react-select__control css-c2frko-control'])[1]"
        searchbox=wait.until(EC.presence_of_element_located(searchbox))
        searchbox.click()


        time.sleep(2)
        options=By.CSS_SELECTOR,".css-fygc7l-option"
        options=wait.until(EC.presence_of_all_elements_located(options))
        chosse=random.choice(options)
        item_chossen.append(chosse.text)
        log.info(f"item chosen for search is {chosse.text}")
        chosse.click()
        
        time.sleep(2)
        searcheduser=By.XPATH,"//div[@class='react-select__single-value css-1n081kd-singleValue']/span"
        searcheduser=wait.until(EC.presence_of_all_elements_located(searcheduser))
        for i in searcheduser:
            log.info(f"verifying the search item {i.text}")
            item_choosed.append(i.text)
        log.info(item_choosed)
        assert item_chossen.__contains__(item_choosed),"item not found in search results"


    def test_view_all_redirections(self):
        log = self.getLogger()
        wait=WebDriverWait(self.driver,20)
        time.sleep(5)
        view_all_buttons_text=By.XPATH,"//div[@class='md:col-span-1 flex flex-col']/div/div/a"
        view_all_buttons_t=wait.until(EC.presence_of_all_elements_located(view_all_buttons_text))
        text_button=random.choice(view_all_buttons_t)
        link=text_button.get_attribute("href")
        text_button.click()
        time.sleep(5)
        current_url=self.driver.current_url
        log.info(f"verifying the redirection link {link} with current url {current_url}")
        assert link==current_url,"redirection link is not matching with current url"   


        
        
    
        
        
        
        
