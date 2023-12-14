from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ITEM = (By.CSS_SELECTOR, "[aria-label='cart item ready to fulfill']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@then('Verify there is an item added to cart')
def item_added_to_cart(context):
    context.driver.find_element(*CART_ITEM), f'Error! Item not added to cart'

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has the correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f'Expected {context.product_name}, but got {actual_name}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    summary_text = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in summary_text, f"Expected '{amount} item' not in {summary_text}"