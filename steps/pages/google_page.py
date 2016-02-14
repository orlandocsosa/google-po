from abstract_page import AbstractPage
from locators.results_locator import GoogleResultsLocator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage(AbstractPage):
    def enter_text(self, text):
        pass
