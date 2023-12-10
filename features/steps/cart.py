from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ITEM = (By.CSS_SELECTOR, "[aria-label='cart item ready to fulfill']")

@then('Verify there is an item added to cart')
def item_added_to_cart(context):
    context.driver.find_element(*CART_ITEM), f'Error! Item not added to cart'