from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, "[class*=UtilityHeaderWrapper]")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
CART_MESSAGE = (By.CSS_SELECTOR, ".styles__StyledRow-sc-wmoju4-0 .styles__StyledHeading-sc-1xmf98v-0")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Click on Target Circle on top header')
def open_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)

@when('Click on cart icon')
def cart_icon(context):
    context.app.main_page.cart_icon()


@then("Verify 'Your cart is empty' message is shown")
def empty_cart(context):
    context.app.cart_page.empty_cart()

@when("Click Sign In")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3").click()


@when("From right side nav menu click Sign in")
def nav_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn'] .styles__ListItemText-sc-diphzn-1").click()


@then("Verify header is present")
def verify_header_present(context):
    context.driver.find_element(*HEADER)


@then("Verify header has {number} links")
def verify_header_present(context, number):
    links = context.driver.find_elements(*HEADER_LINKS)
    #Find elements will always return [], or web elements numbered
    #Find elements will never fail, you must check for something to "pass" or "fail" and you will miss bug
    print(links)
    assert len(links) == int(number), f'Expected {number} links, but got {len(links)}'