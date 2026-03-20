import json
import pytest
from selenium import webdriver
# from seleniumwire import webdriver  # Import from seleniumwire to enable request capturing
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
    
    
    driver =webdriver.Firefox()
    driver.get(base_url)
    # request.cls.base_url = base_url  # Attach base URL to test class
    log=logging.getLogger()

   

    
    time.sleep(10)
    
    driver.find_element(By.NAME,"email").send_keys(os.getenv("USER_NAME"))
    driver.find_element(By.NAME,"password").send_keys(os.getenv("PASSWORD"))
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    # response=requests.get(os.getenv("response"))
    # status=response.status_code
    log=logging.getLogger()
    # log.info(status)
    # Attach driver to test class
    request.cls.driver = driver

    yield driver  # Provide driver instance for tests

    
    # server_errors = []

    # logs = driver.get_log("performance")

    # for entry in logs:
    #     message = json.loads(entry["message"])["message"]

    #     if message["method"] == "Network.responseReceived":
    #         response = message["params"]["response"]
    #         status = response["status"]
    #         url = response["url"]

    #         if status >= 500:
    #             log.error(f"❌ API FAILURE | {url} | Status: {status}")
    #             server_errors.append(f"{url} -> {status}")



    driver.quit()  # Cleanup after tests

    # if server_errors:
    #     pytest.fail(
    #         "❌ API 5xx errors detected:\n" + "\n".join(server_errors),
    #         pytrace=False
    #     )

