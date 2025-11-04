import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from M_tacker.Config.config_reader import read_config
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import requests
from Smoke_tests.utilities.base_class import logging
load_dotenv()  # Load environment variables from .env file

@pytest.fixture(scope="class")
def setup(request):
    
    # Read base URL from config
    base_url = read_config("URL","base_url")
    
    driver =webdriver.Chrome()
    driver.get(base_url)
    time.sleep(10)
    driver.find_element(By.NAME,"email").send_keys(os.getenv("USER_NAME"))
    driver.find_element(By.NAME,"password").send_keys(os.getenv("PASSWORD"))
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    response=requests.get("https://www.google.com/recaptcha/api2/reload?k=6LcoGX0qAAAAAHhaCgPR9ylacU9-92RBegM9HdFa")
    status=response.status_code
    log=logging.getLogger()
    log.info(status)
    # Attach driver to test class
    request.cls.driver = driver

    yield driver  # Provide driver instance for tests

    driver.quit()  # Cleanup after tests
