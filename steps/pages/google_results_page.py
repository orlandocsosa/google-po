from abstract_page import AbstractPage
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from locators.results_locator import GoogleResultsLocator
import sys

class GoogleResultsPage(AbstractPage):
    def get_url(self):
        return 'www.google.com.au/search?q='

    def get_search_results_count(self):
        elements = self.driver.find_elements(*GoogleResultsLocator.SEARCH_RESULTS)
        return len(elements)

    def is_no_results_title_present(self):
        try:
            element = self.driver.find_element(*GoogleResultsLocator.NO_RESULTS)
        except NoSuchElementException as el_err:
            return False

        return True

    def has_results(self):
        count = self.get_search_results_count()
        is_title_present = self.is_no_results_title_present()
        has_results = count > 0
        return has_results and not is_title_present

    def has_no_results(self):
        return not self.has_results()
