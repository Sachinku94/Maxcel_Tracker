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

    def test_CreateUserBulk(self):  #need to check
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
        
    def test_userreport(self):
        log=self.getLogger()
        time.sleep(10)
        user=HomePage.Userreport(self)
        self.driver.get(user)
        time.sleep(5)


    def test_createUserSingle(self):
        wait=WebDriverWait(self.driver,20)
        log=self.getLogger()
        time.sleep(10)
        user=HomePage.User(self)
        self.driver.get(user)
        time.sleep(5)
        single_click=self.driver.find_element(By.XPATH,"//div/div/div/button[@class='themeBtn flex w-full md:w-auto']")
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
                email_field.send_keys(row.Email)
                full_name.send_keys(row.Name)
                Employee_id.send_keys(row.Employee_ID)

        flat_data = []

        for _, row in user_data.iterrows():
            flat_data.extend([row['Role'], row['Shift'], row['Department'],row['Work Type']])

        #"//div[@class='flex lg:grid flex flex-col lg:grid-cols-12 gap-4 mb-[24px] font-semibold']/div/div/div"
        input=By.XPATH,"//div[@class='flex flex-wrap items-start gap-4 w-full mb-4']/div/div"
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
                

                
    def test_filteruser(self):
        log=self.getLogger()
        time.sleep(10)
        user=HomePage.User(self)
        self.driver.get(user)
        time.sleep(5)
        filter_buttons=self.driver.find_elements(By.CSS_SELECTOR,".css-c2frko-control")
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxel_tracker/M_tacker/sample_user.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []

        for _, row in user_data.iterrows():
            flat_data.extend([row['role'], row['department'], row['user'], row['shift'],row['device']])
        
        for filter_button,value in zip(filter_buttons, flat_data):
            try:
                filter_button.click()
                time.sleep(2)
                # filter_input=self.driver.find_element(By.CSS_SELECTOR,".css-1d8n9bt-input")
                # filter_input.send_keys(row.name)
                time.sleep(2)
                options=self.driver.find_elements(By.CSS_SELECTOR,".css-144zqx9 div")
                n=0
                for option in options:
                    log.info(f"clicking on filter option {option.text}")
                    log.info(f"comparing {option.text} with {value}")
                    if option.text==value:
                        log.info(f"Clicking on option: {option.text}")
                        option.click()
                        log.info(f"Selected value: {value}")
                        break
                    
                time.sleep(5)
            except NoSuchElementException as e:
                log.error(f"Element not found: {e}")
            except StaleElementReferenceException as e:
                log.error(f"Stale element reference: {e}")

        
    
    def test_useractions(self):

        log = self.getLogger()
        wait = WebDriverWait(self.driver, 20)

        time.sleep(10)
        user = HomePage.User(self)
        self.driver.get(user)
        time.sleep(5)

        ac = AC(self.driver)

        action_butt = (By.CSS_SELECTOR, "div.MenuOuterDrop.supertab")
        action_button = wait.until(EC.presence_of_all_elements_located(action_butt))

        time.sleep(10)
        random.choice(action_button).click()

        opt = (By.XPATH, "//ul/div/li[@role='menuitem']/span")
        options = wait.until(EC.presence_of_all_elements_located(opt))
        n=0
        try:
            for option in options:
                if n > 5:
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

                if action_text == "Deactivate":
                    time.sleep(2)
                    confirm = self.driver.find_element(
                        By.XPATH, "//div[contains(text(), 'User Deactivated Successfully')]"
                    )
                    assert confirm.text == "User Deactivated Successfully"
                    log.info("User deactivated successfully")

                elif action_text == "Track" or action_text == "Un-track":
                    time.sleep(2)
                    confirm = self.driver.find_element(
                        By.XPATH,
                        "//div[contains(text(), 'User Tracking Setting Changed Successfully')]",
                    )
                    assert confirm.text == "User Tracking Setting Changed Successfully"
                    log.info("User tracking setting changed successfully")

                elif action_text == "Edit":
                    time.sleep(2)
                    confirm = self.driver.find_element(
                        By.XPATH,
                        "//div[@class='relative bg-white rounded-lg shadow-lg z-50 w-full max-w-[1040px]']",
                    )
                    assert confirm.is_displayed()
                    log.info("edit user screen opened successfully")
                    self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()
                    time.sleep(2)   

                elif action_text == "Info":
                    time.sleep(2)
                    confirm = self.driver.current_url
                    assert "organisation/dashboard/users" in confirm
                    log.info("navigated to user info page successfully")
                    self.driver.get(user)
                    log.info("navigated back to user page successfully")
                    current_url = self.driver.current_url
                    log.info(f"current url after navigating back: {current_url}")   
                    time.sleep(5)

                elif action_text == "Disable Password" or action_text == "Enable Password":
                    time.sleep(2)
                    if action_text == "Disable Password":
                        confirm = self.driver.find_element(
                            By.XPATH,
                            "//div[contains(text(), 'Password Disabled Successfully')]",
                        )
                        assert confirm.text == "Password Disabled Successfully"
                    else:
                        confirm = self.driver.find_element(
                            By.XPATH,
                            "//div[contains(text(), 'Password Enabled Successfully')]",
                        )
                        assert confirm.text == "Password Enabled Successfully"
                    log.info("Password enabled/disabled successfully")

                elif action_text == "Logs":
                    time.sleep(5)
                    confirm = self.driver.current_url
                    assert "organisation/dashboard/logs/log-by-chart" in confirm
                    log.info("navigated to user logs page successfully")
                    self.driver.get(user)
                    log.info("navigated back to user page successfully")
                    current_url = self.driver.current_url
                    log.info(f"current url after navigating back: {current_url}")
                    time.sleep(5)

                elif action_text == "Force Logout":
                    time.sleep(2)
                    confirm = self.driver.find_element(
                        By.XPATH,
                        "//div[contains(text(), 'User Logged Out Successfully')]",
                    )
                    assert confirm.text == "User Logged Out Successfully"
                    log.info("User force logged out successfully")

                time.sleep(10)
                time.sleep(10)
                log.info(action_text)
                if action_text == "Info" or action_text=="Logs":
                    log.info(f"Already navigated to {action_text} page, no need to click action button again.")
                    current_url= self.driver.current_url
                    assert "organisation/dashboard/users" in current_url or "organisation/dashboard/logs/log-by-chart" in current_url
                    log.info(f"Current URL after {action_text} action: {current_url}")
                    if current_url != user:
                        self.driver.get(user)
                        log.info("Navigated back to user page successfully")
                    time.sleep(5)
                
                
                try:
                    random.choice(action_button).click()
                except Exception as e:
                    log.error(f"Exception occurred while clicking action button: {e}")
                    if e == True:
                        self.driver.get(user)
                        random.choice(action_button).click()
                time.sleep(5)
                n+=1
            log.info("Completed user actions test successfully")
        except Exception as e:
            log.error(f"Exception occurred during user actions test: {e}")
            self.driver.get(user)