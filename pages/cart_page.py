from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def empty_cart(self):
        actual_message = self.find_element(*self.CART_MESSAGE).text
        expected_message = 'Your cart is empty'
        assert actual_message == expected_message, f'Expected {expected_message} but got {actual_message}'