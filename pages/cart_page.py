from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_HEADER = (By.ID, 'sc-active-items-header')
    ADDED_PRODUCT_LINK = (By.CSS_SELECTOR, 'a.a-link-normal.sc-product-link')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[data-feature-id="item-delete-button"]')
    CART_IMG_COUNT = (By.ID, 'nav-cart-count')
    MAIN_LOGO = (By.ID, 'nav-logo-sprites')
    cart_header = 'Alışveriş Sepeti'
    cart_count = '0'

    def is_cart_header_present(self):
        return  self.get_text(self.CART_HEADER)

    def check_product_id_in_link(self, product_id):
        # checks if the given product id is present in the current url
        # find the <a> element and check if product id is in its href value
        link_element = self.find(*self.ADDED_PRODUCT_LINK)
        href_value = link_element.get_attribute('href')
        return product_id in href_value

    def click_delete_button(self):
        self.click_element(*self.DELETE_BUTTON)

    def is_product_deleted(self):
        # used to check if the product is deleted from the cart
        # returns the count on the cart image
        return self.get_text(self.CART_IMG_COUNT)

    def click_main_header_logo(self):
        self.click_element(*self.MAIN_LOGO)
