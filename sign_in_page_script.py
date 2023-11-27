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
#driver.maximize_window()

#Test Case: Logged out user sees Sign in page when clicking Orders

# Step 1: Open webpage
driver.get('https://www.amazon.com')

#Step 2: Click on orders
driver.find_element(By.ID, 'nav-orders').click()

#Verify Sign in page opens
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

#Verify email field present
driver.find_element(By.ID, 'ap_email')



