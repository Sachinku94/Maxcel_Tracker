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

    def test_CreateUserBulk(self):
        log=self.getLogger()
        time.sleep(10)
        user=HomePage.User(self)
        self.driver.get(user)
        time.sleep(5)
        upload_click=self.driver.find_element(By.CSS_SELECTOR,".themeBtnWhiteOutline")
        upload_click.click()
        bulk=self.driver.find_element(By.XPATH,"//button[contains(text(),'Choose File')]")
        bulk.click()
        file_name="/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample.xlsx"
        log.info(file_name)

        abs_path=os.path.abspath(file_name)
        log.info(abs_path)
        pyperclip.copy(abs_path)
        log.info("file path copied to clipboard")
        pyautogui.hotkey('command', 'v')
        log.info("file path pasted in the dialog box")  
        pyautogui.press('return')
        log.info("pressed enter key")
        # Script worked on mac 0s when accessiblity premission given to vs code or terminal


        time.sleep(3)

        done=self.driver.find_element(By.XPATH,"//button[contains(text(),'Send Invitations')]")
        done.click()

    def test_createUserSingle(self):
        wait=WebDriverWait(self.driver,20)
        log=self.getLogger()
        time.sleep(10)
        user=HomePage.User(self)
        self.driver.get(user)
        time.sleep(5)
        single_click=self.driver.find_element(By.CSS_SELECTOR,".themeBtn:nth-child(2)")
        single_click.click()
        time.sleep(3)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample.xlsx")
        count=len(user_data)
        log.info(f"Total number of users to be created: {len(user_data)}")
        n=0
        if count>0:
                add_user=self.driver.find_element(By.XPATH,"//button[contains(text(),'+ Add Another Employee')]")
                while n!=count-1:
                    
                 add_user.click()
                 time.sleep(2)
                 n+=1
                 
                 log.info(count)
        email_fields=self.driver.find_elements(By.XPATH,"//input[@placeholder='Employee Email']")
        full_names=self.driver.find_elements(By.XPATH,"//input[@placeholder='Full Name']")
        Employee_ids=self.driver.find_elements(By.XPATH,"//input[@placeholder='Employee ID']")
        for row, email_field,full_name, Employee_id in zip(user_data.itertuples(index=False), email_fields, full_names, Employee_ids):
                email_field.send_keys(row.email)
                full_name.send_keys(row.name)
                Employee_id.send_keys(row.employeeId)

        flat_data = []

        for _, row in user_data.iterrows():
            flat_data.extend([row['role'], row['shift'], row['department']])

        #"//div[@class='flex lg:grid flex flex-col lg:grid-cols-12 gap-4 mb-[24px] font-semibold']/div/div/div"
        input=By.XPATH,"//div[@class='flex flex-col col-span-2']/div/div"
        input_fields = wait.until(EC.presence_of_all_elements_located(input))

        # Debugging output
        log.info(f"Total flat_data values: {len(flat_data)}")
        log.info(f"Total input fields found: {len(input_fields)}")

        if len(flat_data) != len(input_fields):
            log.warning("Mismatch between flat_data and input_fields. Check your XPath or data.")
        else:
            for value, field in zip(flat_data, input_fields):
                field.click()
                time.sleep(2)
                # self.driver.execute_script(f"document.querySelector('select.form-control').value = {value};")
                drop_down=self.driver.find_elements(By.CSS_SELECTOR,".css-fygc7l-option")
                for option in drop_down:
                    if option.text==value:
                        log.info(f"Clicking on option: {option.text}")
                        option.click()
                        log.info(f"Selected value: {value}")
                        break
                time.sleep(5)
                

                


        

