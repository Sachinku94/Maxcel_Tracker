from cmath import log
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
import allure
from allure_commons.types import AttachmentType
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
    time.sleep(10) # wait is only to find 500 error in logs

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

# ==============================================================================
# HOOK TO CAPTURE SCREENSHOT & LOGS ON FAILURE OR 500 ERRORS (CHROME & FIREFOX)
# ==============================================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    log=logging.getLogger()

    # CONDITION 1: Test failed at any stage (setup, call, teardown)
    is_failed = rep.failed 
    
    # We will compute Condition 2 and Condition 3 below
    is_500_error = False
    browser_logs = []
    
    driver = None
    if item.cls and hasattr(item.cls, "driver"):
        driver = item.cls.driver

    # Scan for 500 triggers actively if the driver is live
    if driver:
        # Check browser name to apply the correct strategy
        browser_name = driver.capabilities.get("browserName", "").lower()

        # --- CHROME STRATEGY ---
        if "chrome" in browser_name:
            try:
                # CONDITION 2: Scan Chrome's active console for 500 errors
                fetched_logs = driver.get_log("browser")
                for entry in fetched_logs:
                    log_line = f"{entry['level']} - {entry['message']}"
                    browser_logs.append(log_line)
                    
                    if "500" in entry["message"]:
                        is_500_error = True

                # Optional: Scan Chrome's Performance logs for background API 500s
                perf_logs = driver.get_log("performance")
                for entry in perf_logs:
                    message = json.loads(entry["message"])["message"]
                    if message.get("method") == "Network.responseReceived":
                        status = message["params"]["response"]["status"]
                        if status >= 500:
                            is_500_error = True
                            browser_logs.append(f"❌ API 500 Detected: {message['params']['response']['url']}")

            except Exception:
                pass # Fallback if logging fails

        # --- FIREFOX STRATEGY (And fallback for Chrome) ---
        # CONDITION 3: Read page source to check for a rendered 500 error page
        try:
            page_content = driver.page_source
            rendered_500_indicators = [
                "500 Internal Server Error", 
                "Server Error", 
                "500 error", 
                "Something went wrong"
            ]
            
            if any(indicator in page_content for indicator in rendered_500_indicators):
                is_500_error = True
                log.info(f"🔍 Detected potential 500 error in page source of {item.name}")
        except Exception:
            pass


    # EXECUTE ALLURE ATTACHMENTS IF ANY OF THE 3 CONDITIONS ARE MET
    if is_failed or is_500_error:
        if driver:
            try:
                # 1. Take Screenshot and attach to Allure
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_{rep.when}_{item.name}",
                    attachment_type=AttachmentType.PNG
                )

                # 2. Attach Browser Console Logs (Highly effective on Chrome)
                if browser_logs:
                    allure.attach(
                        "\n".join(browser_logs),
                        name=f"Console_Logs_{item.name}",
                        attachment_type=AttachmentType.TEXT
                    )

                # 3. Attach full HTML Page Source (Perfect for rendering Firefox 500 pages)
                allure.attach(
                    driver.page_source,
                    name=f"HTML_Source_{item.name}",
                    attachment_type=AttachmentType.TEXT
                )
                
                log.info(f"\n[Allure] Automated captures triggered on {rep.when} phase.")

            except Exception as e:
                log.info(f"\n[Allure] Failed to run automated captures: {e}")