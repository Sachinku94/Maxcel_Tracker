# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Step 1: Setup WebDriver
# driver = webdriver.Chrome()
# driver.maximize_window()

# # Step 2: OAuth Authorization URL
# auth_url = (
#     "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?"
#     "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
#     "redirect_uri=https%3A%2F%2Fstg-fe.maxeltracker.com%2Fapi%2Fauth%2Fgoogle%2Fcallback&"
#     "response_type=code&"
#     "scope=openid%20email%20profile&"
#     "access_type=offline&"
#     "prompt=consent&"
#     "service=lso&"
#     "o2v=2&"
#     "flowName=GeneralOAuthFlow"
# )

# # Step 3: Navigate to OAuth URL
# driver.get(auth_url)

# # Step 4: Simulate Google Login (if not already logged in)
# # You may need to manually log in or automate login if test credentials are available
# # Example (only works if login page is shown):
# # driver.find_element(By.ID, "identifierId").send_keys("your-email@gmail.com")
# # driver.find_element(By.ID, "identifierNext").click()
# # time.sleep(2)
# # driver.find_element(By.NAME, "password").send_keys("your-password")
# # driver.find_element(By.ID, "passwordNext").click()

# # Step 5: Wait for Redirect
# time.sleep(10)  # Adjust based on network speed and login flow

# # Step 6: Capture Redirect URL
# redirected_url = driver.current_url
# print("Redirected URL:", redirected_url)

# # Step 7: Validate Authorization Code
# if "code=" in redirected_url:
#     print("✅ Authorization code received.")
# else:
#     print("❌ Authorization code not found.")

# # Step 8: Cleanup
# driver.quit()


from selenium import webdriver
import time

# Step 1: Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Tamper the redirect_uri in the OAuth URL
tampered_url = (
    "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?"
    "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
    "redirect_uri=https%3A%2F%2Fmalicious-site.com%2Fcallback&"  # <-- Tampered URI
    "response_type=code&"
    "scope=openid%20email%20profile&"
    "access_type=offline&"
    "prompt=consent&"
    "service=lso&"
    "o2v=2&"
    "flowName=GeneralOAuthFlow"
)

# Step 3: Navigate to the tampered URL
driver.get(tampered_url)

# Step 4: Wait for Google's error response
time.sleep(5)

# Step 5: Capture and print the current URL or error page
current_url = driver.current_url
print("Redirected to:", current_url)

# Step 6: Check for redirect_uri_mismatch error
if "error" in current_url or "redirect_uri_mismatch" in current_url:
    print("✅ Negative test passed: Redirect URI mismatch detected.")
else:
    print("❌ Negative test failed: No error detected.")

# Step 7: Cleanup
driver.quit()