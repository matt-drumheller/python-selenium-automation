from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
SIZE_OPTION = (By.CSS_SELECTOR, '[class*="styles__ButtonWrapper-sc"] [value="S"]')


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)


# @then('Verify user can click through colors')
# def click_and_verify_colors(context):
#     expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
#     for color in colors:
#         color.click()
#         selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]  # 'Color\nBlack' => ['Color', 'Black']
#         actual_colors.append(selected_color)
#
#     assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

@when ('Select size small')
def size_selector(context):
    context.driver.find_element(*SIZE_OPTION).click()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Brown', 'Light Gray', 'Burgundy', 'Dark Green', 'Dark Gray', 'Tan']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'