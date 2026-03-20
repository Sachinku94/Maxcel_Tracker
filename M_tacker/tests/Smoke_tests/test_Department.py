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


    def test_Departmentsearch(self):
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.department(self)
        self.driver.get(app)
        time.sleep(5)
        
        time.sleep(2)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_1.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        filter_but=By.XPATH,"//input[@placeholder='Search Departments']"
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

    def test_DepartmentCreation(self):
        # try:
        #         current_url = self.driver.current_url
        #         response=requests.get(current_url)
        #         status=response.status_code
                
        #         if status == 500:
        #             log.error(f"Server error occurred: {current_url}")
        #         else:
        #             log.info(f"Current URL: {current_url} - Status Code: {status}")
        # except Exception as e:
        #     pass
        log = self.getLogger()


        # for request in self.driver.requests:

        #   if request.response:
        #      log.info(
        #     f"API: {request.url} | "
        #     f"Method: {request.method} | "
        #     f"Status: {request.response.status_code}"
        # )

        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.department(self)
        self.driver.get(app)
        time.sleep(5)
        # find_element=By.XPATH,"//div[@class='flex items-center gap-2 cursor-pointer']"
        # find=wait.until(EC.element_to_be_clickable(find_element))
        # find.click()
        
        create_but=By.CSS_SELECTOR,".themeBtn"
        create_button=wait.until(EC.element_to_be_clickable(create_but))
        create_button.click()
        time.sleep(2)
        dept_name=By.CSS_SELECTOR,".transition"
        dept_name=wait.until(EC.presence_of_all_elements_located(dept_name))
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_user.xlsx")
        count=len(user_data)
        op_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_2.xlsx")
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        opt_data=[]
        for _, row in op_data.iterrows():
            opt_data.extend([row['tags'], row['user'], row['department']])
        for _, row in user_data.iterrows():
            flat_data.extend([ row['department'], row['user']])
        for value, field in zip(flat_data, dept_name):
               field.click()
               field.send_keys(value)
               time.sleep(5)
        time.sleep(5)      
        tgs=By.CSS_SELECTOR,".css-19bb58m"
        tgs=wait.until(EC.presence_of_all_elements_located(tgs))
        send_data=By.CSS_SELECTOR,".css-19bb58m input"
        send_button=wait.until(EC.visibility_of_any_elements_located(send_data))
        for value, field, send in zip(opt_data, tgs, send_button):
            field.click()
            time.sleep(3)

            log.info(f"Entering value: {value}")

            send.send_keys(value)


            time.sleep(3)

            drop_down = self.driver.find_elements(By.CSS_SELECTOR, ".css-fygc7l-option")
            for option in drop_down:
                if option.text.strip() == value:
                    option.click()
                    log.info(f"Selected value: {value}")
                    break

            time.sleep(2)

    def test_Departmentaction(self):
        log = self.getLogger()
        time.sleep(10)
        wait=WebDriverWait(self.driver,20)
        app=HomePage.department(self)
        self.driver.get(app)
        time.sleep(5)
        action_btt=By.CSS_SELECTOR,"div.MenuOuterDrop.supertab"
        action_button=wait.until(EC.presence_of_all_elements_located(action_btt))
        time.sleep(10)
        random.choice(action_button).click()

        opt = (By.XPATH, "//ul/div/li[@role='menuitem']/span")
        options = wait.until(EC.presence_of_all_elements_located(opt))
        n=0
        try:
            for option in options:
                if n > 3:
                    break
                log.info(f"clicking on action option {option.text}")

                time.sleep(10)
                random_ch = random.choice(options)

                # ✅ normalize text (previous fix preserved)
                action_text = random_ch.text.strip()
                log.info(f"clicked on action option [{action_text}]")

                # ✅ FIX: prevent MoveTargetOutOfBoundsException
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    random_ch,
                )
                self.driver.execute_script("arguments[0].click();", random_ch)

                if action_text == "Edit Department":
                    time.sleep(2)
                    confirm = self.driver.find_element(
                        By.CSS_SELECTO, ".rounded-lg"
                    )
                    assert confirm.is_displayed(), "Edit department modal did not appear"
                    log.info("Edit department modal appeared successfully")

                elif action_text == " Manage Productivity":
                    time.sleep(2)
                    confirm = self.driver.current_url
                    assert "productivity" in confirm, "Did not navigate to productivity page"
                    log.info("Navigated to productivity page successfully")
                    time.sleep(5)
                    self.driver.get(app)  # Navigate back to the department page
                    time.sleep(5)
                    log.info("navigated back to dept page successfully")
                    current_url = self.driver.current_url
                    log.info(f"current url after navigating back: {current_url}")
                    time.sleep(5)
                elif action_text == "Delete":
                    time.sleep(2)
                    
                    confirm = self.driver.find_element(
                        By.CSS_SELECTOR,
                        ".rounded-lg",
                    )
                    assert confirm.is_displayed()
                    log.info("edit user screen opened successfully")
                    self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()
                    time.sleep(2)
                    log.info("Delete confirmation appeared successfully")
                    

               
                time.sleep(5)
                n+=1
            log.info("Completed user actions test successfully")
        except Exception as e:
            log.error(f"Exception occurred during user actions test: {e}")
            self.driver.get(app)
            
        
