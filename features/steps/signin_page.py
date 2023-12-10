from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@then("Verify Sign in form opens")
def sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__ContentWrapper-sc-19gc5cv-1")