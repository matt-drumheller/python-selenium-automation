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

# open the url
driver.get('https://www.amazon.com')

#amazon logo
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")

#Create account
driver.find_element(By.CSS_SELECTOR, ".a-box .a-spacing-small")

#Your name box
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#Mobile/Email box
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Password box
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#Password character limit notice
driver.find_element(By.CSS_SELECTOR, ".a-alert-inline-info .a-alert-content")

#Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#Continue/create button
driver.find_element(By.CSS_SELECTOR, "#continue")

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice?ie=UTF']")

#Sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")