from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART = (By.ID, 'addToCartButtonOrTextIdFor53740849')
POP_UP_WINDOW = (By.CSS_SELECTOR, "[class*='styles__StyledButton-sc']")

@then('Verify search worked for {search_result}')
def verify_search(context, search_result):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert search_result in search_results_header, f'Expected text {search_result} not in {search_results_header}'


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} not in {context.driver.current_url}'


@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

@when('CLose pop up window')
def pop_up_window(context):
    context.driver.find_element(*POP_UP_WINDOW).click()



