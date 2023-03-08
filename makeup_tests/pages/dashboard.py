from typing import Tuple
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from makeup_tests.pages.main_page import MainPage


class Dashboard(MainPage):

    def __init__(self, driver: Chrome):
        super().__init__(driver)

    def select_category(self, category_name):
        """

        :param category_name: select category name
        :return: category name
        """
        category_locator: Tuple[By.XPATH, str] = (By.XPATH, f"//a[@class='menu-list__link'][contains(text(),'{category_name}')]")
        self.focus(category_locator)

    def select_sub_category(self, sub_category_name):
        """

        :param sub_category_name: select sub category name
        :return: sub category name
        """
        sub_category_locator: Tuple[By.XPATH, str] = (By.XPATH, f"//a[contains(text(),'{sub_category_name}')]")
        self.click(sub_category_locator)

    def choose_item(self, item_name):
        '''

        :param item_name: select item
        :return: item
        '''
        item_selection: Tuple[By.XPATH, str] = (By.XPATH, f"(//a[contains(text(),'{item_name}')])[1]")
        self.click(item_selection)
