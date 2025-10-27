import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from M_Tracker.Config.config_reader import read_config
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
load_dotenv()  # Load environment variables from .env file

@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    base_url = read_config("URL","base_url")
    # CHROMEDRIVER_VERSION = "132.0.6834.110"

    # path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
    # Set up Chrome options for headless execution in Docker
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")  # Required for running in Docker
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    # chrome_options.add_argument(
    #     "--disable-dev-shm-usage"
    # )  # Overcome memory limitations
    # chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
    # chrome_options.add_argument(
    #     "--window-size=1920,1080"
    # )  # Ensure consistent resolution

    # Initialize WebDriver
    # service = Service(path)
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open base URL
    driver =webdriver.Chrome()
    driver.get(base_url)
    time.sleep(10)
    driver.find_element(By.NAME,"email").send_keys(os.getenv("USER_NAME"))
    driver.find_element(By.NAME,"password").send_keys(os.getenv("PASSWORD"))
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    # Attach driver to test class
    request.cls.driver = driver

    yield driver  # Provide driver instance for tests

    driver.quit()  # Cleanup after tests
