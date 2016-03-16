from selenium import webdriver
from abc import ABCMeta


class AbstractPage(object):
    __metaclass__ = ABCMeta

    def __init__(self, driver):
        self.driver = driver
        """:type : webdriver.Remote """

    def wait(self, time):
        self.driver.implicitly_wait(time)
