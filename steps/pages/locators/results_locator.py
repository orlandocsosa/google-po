from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By

class GoogleResultsLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.srg .g')
    NO_RESULTS = (By.CSS_SELECTOR, '.med > p')