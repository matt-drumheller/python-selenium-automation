from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test*='addToCartButton']")
POP_UP_WINDOW = (By.CSS_SELECTOR, "[class*='styles__StyledButton-sc']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)


@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('CLose pop up window')
def pop_up_window(context):
    context.driver.find_element(*POP_UP_WINDOW).click()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # find_element by default it will pick 1st one
    # all_buttons = context.driver.find_elements(*ADD_TO_CART_BTN)
    # all_buttons[2].click()

@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text

@then('Verify search worked for {product}')
def verify_search(context, product):
    context.app.search_results_page.verify_search(product)


