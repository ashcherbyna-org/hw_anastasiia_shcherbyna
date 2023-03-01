from datetime import time
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome("drivers/chromedriver")


def test_search():
    driver.get("https://makeup.com.ua/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "search-input").send_keys("мыло")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    driver.close()



