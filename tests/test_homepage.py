import time
from core.browser import Browser
from pages.Homepage import HomePage
from config import URL, WAIT_TIME

def run_test():
    # Launch browser
    driver = Browser.start_browser()

    # Open website
    driver.get(URL)

    # Click button
    home_page = HomePage(driver)
    home_page.click_explore_matlab()

    # Wait to see result
    time.sleep(WAIT_TIME)

    # Close browser
    Browser.close_browser(driver)

if __name__ == "__main__":
    run_test()
