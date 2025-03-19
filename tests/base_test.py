import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'
    COOKIES_REJECT = (By.ID, 'sp-cc-rejectall-link')

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications") #disable notifications to avoid interruptions on page
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com.tr/')
        self.driver.implicitly_wait(10)
        # reject the cookies pop-up
        time.sleep(2)
        self.driver.find_element(*self.COOKIES_REJECT).click()

    def tearDown(self):
        self.driver.quit()