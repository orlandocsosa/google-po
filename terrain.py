from lettuce import world, before, after
from selenium import webdriver


@before.all
def setup_browser():
    world.browser = webdriver.Firefox()


@after.all
def close_browser(total_result):
    world.browser.close()
    world.browser.quit()

