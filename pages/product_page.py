import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    SELECT_QUANTITY = (By.ID, 'selectQuantity') # select quantity dropdown bar
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    CART_IMG_COUNT = (By.ID, 'nav-cart-count')
    CART_IMG = (By.ID, 'nav-cart')
    cart_count = '1'
    product_id = ''

    def add_product_to_cart(self):
        # add the product to cart by clicking on the add to cart button
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def get_product_id(self):
        # get the product id, update the corresponding variable
        current_url = self.get_current_url() # get the current url
        match = re.search(r"/dp/([A-Z0-9]{10})", current_url)  # extract product id using regex pattern
        if match:
            self.product_id = match.group(1)  # Update the product_id variable
        return self.product_id  # Return the extracted ID (optional)

    def is_product_added(self):
        # used to check if the product is added to cart
        # returns the count on the cart image
        return self.get_text(self.CART_IMG_COUNT)

    def click_cart_icon(self):
        # clicks the cart icon and continues to cart page
        self.click_element(*self.CART_IMG)