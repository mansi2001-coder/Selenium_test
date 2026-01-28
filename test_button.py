from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Launch browser
driver = webdriver.Chrome()

#Open website
driver.get("https://in.mathworks.com/")

#Wait for page to load
time.sleep(3)

#Find button and click
button = driver.find_element(By.LINK_TEXT, "Explore MATLAB")
button.click()

#Wait to see result
time.sleep(5)

#Close browser
driver.quit()

