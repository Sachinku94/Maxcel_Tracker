from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from M_tacker.Config.config_reader import read_config

class HomePage(BaseClass):

    # def __init__(self, driver):
    #     self.driver = driver
    global env_url
    env_url = read_config("env","stg_url")

    def User(self):
        # log= self.getLogger()
        # log.info("Clicking on User tab")
        time.sleep(5)
        # user=self.driver.find_element(By.XPATH,"//span[@class='user-name']")
        user=env_url+"organisation/dashboard/users"
        return user

    def appsandwebsite(self):
        time.sleep(5)
        app_web=env_url+"organisation/dashboard/apps-and-websites"
        return app_web

        
    def screen_shot(self):
        time.sleep(5)
        sc_shot=env_url+"organisation/dashboard/screenshots"
        return sc_shot
    
    def graph_logs(self):
        time.sleep(5)
        sc_shot=env_url+"organisation/dashboard/logs/log-by-chart"
        return sc_shot
    
    def comprehensive_logs(self):
        time.sleep(5)
        sc_shot=env_url+"organisation/dashboard/logs/log-by-date"
        return sc_shot
    
    def cologs(self):
        time.sleep(5)
        co_log=env_url+"organisation/dashboard/logs/log-by-date"
        return co_log   
    
    def productive(self):
        time.sleep(5)
        pro_uct=env_url+"organisation/dashboard/productivity/most-productive"
        return pro_uct
    
    def unproductive(self):
        time.sleep(5)
        un_pro=env_url+"organisation/dashboard/productivity/most-unproductive"
        return un_pro
    
    def ideal(self):
        time.sleep(5)
        id_le=env_url+"organisation/dashboard/productivity/most-idle"
        return id_le    
    
    def best_performer(self):
        time.sleep(5)
        best_per=env_url+"organisation/dashboard/productivity/best-performance"
        return best_per