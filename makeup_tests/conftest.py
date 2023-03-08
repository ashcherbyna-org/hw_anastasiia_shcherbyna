import pytest
from selenium.webdriver import Chrome

from makeup_tests.pages.dashboard import Dashboard
from makeup_tests.pages.item import Item


@pytest.fixture(scope='session')
def driver():
    chrome = Chrome("drivers/chromedriver")

    chrome.get("https://makeup.com.ua/")
    chrome.maximize_window()
    yield chrome
    chrome.quit()


@pytest.fixture(scope='session')
def dashboard(driver):
    yield Dashboard(driver)


@pytest.fixture(scope='session')
def item(driver):
    yield Item(driver)
