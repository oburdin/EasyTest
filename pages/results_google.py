from selenium.webdriver.common.by import By
from pages.start_google import GoogleStart

class ResultsGoogle(GoogleStart):
    def is_first_link_available(self):
        self.first_link_locator = (By.XPATH, '//*[@id="rso"]//a')

        return self.browser.find_element(*self.first_link_locator).is_enabled()

