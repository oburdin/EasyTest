import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OnlyOne():
    instance = None

    def __new__(cls, name):  # The same parameters as in the constructor

        if not OnlyOne.instance:
            return super().__new__(cls)
        else:
            return OnlyOne.instance

    def __init__(self, name):
        OnlyOne.instance = self
        self.name = str(name)


class TestOnlyOne():
    def test1(self):
        a = OnlyOne('qqq')
        b = OnlyOne('ddd')
        assert a is b
        assert a.name == 'ddd'



class TestWikiAnaklitus():
    @pytest.mark.skip(reason='d')
    def test_open_image_anaklitus(self):

        wiki_page = webdriver.Edge()
        wiki_page.get(r'http:\\uk.wikipedia.org')
        assert 'Вікіпедія' in wiki_page.title

        search_field = wiki_page.find_element_by_xpath("//input[@id='searchInput']")
        search_field.send_keys("Список римських пап")
        search_field.send_keys(Keys.RETURN)


        assert 'Cletus' in wiki_page