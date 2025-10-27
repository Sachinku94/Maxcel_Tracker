from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BaseClass):

    # def __init__(self, driver):
    #     self.driver = driver
        

    def User(self):
        # log= self.getLogger()
        # log.info("Clicking on User tab")
        time.sleep(5)
        # user=self.driver.find_element(By.XPATH,"//span[@class='user-name']")
        user="https://stg-fe.maxeltracker.com/organisation/dashboard/users"
        return user



        
    