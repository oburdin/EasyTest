from selenium.webdriver.common.by import By

class GoogleStart():
    def __init__(self, testsetup):
        self.browser = testsetup

        self.search_field_locator = (By.ID, 'lst-ib')


    def click_search_field(self):
        self.browser.find_element(*self.search_field_locator).click()
        return self

    def clear_search_field(self):
        self.browser.find_element(*self.search_field_locator).clear()
        return self

    def input_to_search_field(self, input_text):
        self.browser.find_element(*self.search_field_locator).send_keys(input_text)
        return self

    def submit_search(self):
        self.browser.find_element(*self.search_field_locator).submit()
        return self

