from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage): #inheriting to be able to use the methods
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    search_text = 'samsung'

    def search_samsung(self):
        # this function searches 'samsung' using the search bar
        self.search(self.SEARCH_BAR, self.search_text)
