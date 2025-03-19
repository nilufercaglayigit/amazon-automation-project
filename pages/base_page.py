from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        # initializes itself using driver each time
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        # find element using locator
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        # click element using locator
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        # get the current url of the page
        return self.driver.current_url

    def wait_element(self, method, message=''):
        # wait for the element to be clickable
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        # wait until the element is clickable, then return the text
        return self.wait_element(locator).text

    def search(self, locator, search_text):
        typing_box = self.wait_element(locator) # wait until element is clickable
        typing_box.clear()  # clear any existing text
        typing_box.send_keys(search_text)  # type the search text
        typing_box.send_keys(Keys.RETURN)  # press enter to perform the search

    def scroll_to_element(self, locator):
        # scroll to an element
        element = self.find(*locator)  # find the element
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_existence(self, *locator):
        # checks the existence of a given element
        elements = self.driver.find_elements(*locator) # store if any element found in the elements variable
        return len(self.driver.find_elements(*locator)) > 0 # check for the length of the elements to check existence
