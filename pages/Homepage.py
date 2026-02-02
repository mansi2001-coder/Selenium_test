from selenium.webdriver.common.by import By
import time
from config import WAIT_TIME

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_explore_matlab(self):
        time.sleep(WAIT_TIME)
        button = self.driver.find_element(By.LINK_TEXT, "Explore MATLAB")
        button.click()
