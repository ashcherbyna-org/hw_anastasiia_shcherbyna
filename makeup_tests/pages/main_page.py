from typing import Tuple

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from makeup_tests.core.cookies import Cookies


class MainPage:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.cookies = Cookies(driver)

    def wait_for_element(self, locator: Tuple[By.XPATH, str]):
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator: Tuple[By.XPATH, str]):
        element: WebElement = self.wait_for_element(locator)
        element.click()

    def focus(self, locator: Tuple[By.XPATH, str]):
        action = ActionChains(self.driver)
        element: WebElement = self.wait_for_element(locator)
        action.move_to_element(element).perform()
        self.driver.implicitly_wait(5)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")