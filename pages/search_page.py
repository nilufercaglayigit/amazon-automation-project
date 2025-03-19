from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_KEYWORD_SAMSUNG = (By.CLASS_NAME, 'a-color-state')
    SIMILAR_PRODUCT_CAPTION = (By.XPATH, "//h2[text()='Benzer aramalar']")
    PAGE_NUMBER_2_BUTTON = (By.CSS_SELECTOR, "a[aria-label='2 sayfasına git']")
    SELECTED_PAGE = (By.CSS_SELECTOR, 's-pagination-selected')
    #PRODUCT_IMAGE = (By.CSS_SELECTOR, ".s-main-slot .s-result-item:nth-of-type(5)")
    PRODUCT_IMAGE = (By.XPATH, '(//div[@role="listitem"])[3]')
    # PRODUCT_IMAGE = (By.CSS_SELECTOR, '[class*="widgetId=search-results_3"]')
    page_number_link = 'page=2'
    search_samsung = 'samsung'


    def get_search_keyword_text(self):
        # returns the text of the search keyword
        return self.get_text(self.SEARCH_KEYWORD_SAMSUNG)

    def scroll_to_similar_product(self):
        # scrolls down to similar products caption to be able to see the page selection bar
        self.scroll_to_element(self.SIMILAR_PRODUCT_CAPTION)

    def click_second_page(self):
        # Wait for the second page button to be clickable
        self.wait_element(self.PAGE_NUMBER_2_BUTTON)
        # clicks the page 2 button
        self.click_element(*self.PAGE_NUMBER_2_BUTTON)

    def click_product(self):
        # clicks the product 3rd from top
        self.click_element(*self.PRODUCT_IMAGE)