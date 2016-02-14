from lettuce import world, steps, before
from selenium import webdriver
import lettuce_webdriver.webdriver
from pages.google_results_page import GoogleResultsPage
from abstract_steps import AbstractStep


@steps
class SearchSteps(AbstractStep):
    def then_i_should_see_results(self, step, is_no_in_sentence = None):
        '''I should see (no )?results'''
        positive_test = is_no_in_sentence is None
        page = GoogleResultsPage(self.driver)
        if positive_test:
            result = page.has_results()
        else:
            result = page.has_no_results()

        return result

SearchSteps(world)
