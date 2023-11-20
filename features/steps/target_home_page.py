from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/Cart.svg#Cart']").click()


@then("Verify 'Your cart is empty' message is shown")
def empty_cart(context):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, ".styles__StyledRow-sc-wmoju4-0 .styles__StyledHeading-sc-1xmf98v-0").text
    expected_message = 'Your cart is empty'
    assert actual_message == expected_message, f'Expected {expected_message} but got {actual_message}'


@when("Click Sign In")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3").click()


@when("From right side nav menu click Sign in")
def nav_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn'] .styles__ListItemText-sc-diphzn-1").click()


@then("Verify Sign in form opens")
def sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__ContentWrapper-sc-19gc5cv-1")