from utils.driver_helper import driver
from selenium.webdriver.common.by import By


class RedditHomeScreen:

    search_field_locator_type = By.ID
    search_field_locator = 'my_id_blah'

    def is_open(self):
        search_element = driver.find_element(self.search_field_locator_type, self.search_field_locator)
        if search_element.is_displayed():
            return True
        else:
            return False

    def do_this(self):
        # do something and always return self if doesn't have to return boolean
        return self

    def do_that(self):
        # do something and always return self if doesn't have to return boolean
        return self
