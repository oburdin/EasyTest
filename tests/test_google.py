from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.start_google import GoogleStart
from pages.results_google import ResultsGoogle

class TestGoogleSearch():
    def test_search_requests_submit(self):
        chr = webdriver.Chrome()
        chr.get('http://google.com.ua')

        start_page = GoogleStart(chr)

        start_page.click_search_field() \
            .clear_search_field() \
            .input_to_search_field('вивчити пайтон зараз і без реєстрації безкоштовно') \
            .submit_search()
        results_page = ResultsGoogle(chr)
        assert results_page.is_first_link_available()

