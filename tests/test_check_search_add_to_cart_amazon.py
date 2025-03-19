import time

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestCheckSearchAddToCartAmazon(BaseTest):

    def test_check_search_add_to_cart_amazon(self):

        # HOMEPAGE
        home_page = HomePage(self.driver)
        # check if you are on homepage
        self.assertIn(self.base_url, home_page.get_current_url(), 'You are not on the Amazon TR homepage')
        # search for 'samsung'
        home_page.search_samsung()


        # SEARCH PAGE
        search_page = SearchPage(self.driver)
        # check if results are 'samsung' related
        self.assertIn(search_page.search_samsung, search_page.get_search_keyword_text(), 'You are not seeing results related to Samsung')
        # scroll down to 'similar products' text
        search_page.scroll_to_similar_product()
        # click and go to second page
        search_page.click_second_page()
        # check if you are on second page
        self.assertIn(search_page.page_number_link, search_page.get_current_url(), "You are not on second page")
        # wait and click on the third product from top
        time.sleep(2)
        search_page.click_product()


        # PRODUCT PAGE
        product_page = ProductPage(self.driver)
        # check if you are on product page: check the existence of quantity dropdown
        self.assertTrue(product_page.check_existence(*product_page.SELECT_QUANTITY), 'You are not on the product page')
        # assert product_page.check_existence(*product_page.SELECT_QUANTITY), "You are not on the product page"
        # store the product id
        product_page.get_product_id()
        # add the product to cart: click the add to cart button
        product_page.add_product_to_cart()
        # check if the product is added to cart: check the no. on the cart icon
        self.assertEqual(product_page.cart_count, product_page.is_product_added(), 'The product has not been added to cart')
        # click the cart icon: go to the cart page
        product_page.click_cart_icon()


        #CART PAGE
        cart_page = CartPage(self.driver)
        # check if on cart page
        self.assertIn(cart_page.cart_header, cart_page.is_cart_header_present(), 'You are not on Cart Page')
        # check if correct product has been added to cart: compare it with product_id taken from product_page
        self.assertTrue(cart_page.check_product_id_in_link(product_page.product_id), 'The product in cart is incorrect')
        # delete the product from cart
        cart_page.click_delete_button()
        # check if the product is deleted from the cart: check the no. on the cart icon
        self.assertEqual(cart_page.cart_count, cart_page.is_product_deleted(), 'The product has not been deleted from the cart')
        # click main header logo to go the home page
        cart_page.click_main_header_logo()

        # Back to Home Page
        self.assertIn(self.base_url, home_page.get_current_url(), 'You are not on the Amazon TR homepage')