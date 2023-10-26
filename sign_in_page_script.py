from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#Test Case: Logged out user sees Sign in page when clicking Orders

# Step 1: Open webpage
driver.get('https://www.amazon.com')

#Step 2: Click on orders
driver.find_element(By.ID, 'nav-orders').click()

#Verify Sign in page opens
expected_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

assert expected_result == actual_result, "Error, Sign in header not present"

expected_result_2 = driver.find_element(By.ID, 'ap_email')
actual_result_2 = driver.find_element(By.ID, 'ap_email')

assert expected_result_2 == actual_result_2, "Error, test case failed. Email field not present"
print("Test case passed.")



