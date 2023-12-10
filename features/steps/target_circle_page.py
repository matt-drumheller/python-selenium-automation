from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc']")


@then('Verify there are {number} benefit boxes present')
def verify_benefit_boxes_present(context, number):
    boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(boxes) == int(number), f'Expected boxes is {number}, but got {len(boxes)}'