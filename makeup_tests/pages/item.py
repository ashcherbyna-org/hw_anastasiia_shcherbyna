from selenium.webdriver import Chrome
from makeup_tests.pages.main_page import MainPage
from typing import Tuple
from selenium.webdriver.common.by import By


class Item(MainPage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

    def add_item_basket(self):
        add_to_basket: Tuple[By.XPATH, str] = (By.XPATH, "//div[@class='product-item__button']//div[@class='button "
                                                         "buy'][contains(text(),'Купить')]")
        self.click(add_to_basket)

    def close_pop_up(self):
        '''

        :return: closed pop up
        '''
        close_pop_up: Tuple[By.XPATH, str] = (By.XPATH, "(//div[@class='popup-close close-icon'])[4]")
        self.click(close_pop_up)

    def get_basket_value(self):
        '''

        :return: value from basket
        '''
        basket_value: Tuple[By.XPATH, str] = (By.XPATH, "//span[contains(text(),'Корзина')]")
        element = self.wait_for_element(basket_value)
        return element.find_element(By.TAG_NAME, "span").text




