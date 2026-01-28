from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Launch browser
driver = webdriver.Chrome()

#Open website
driver.get("https://in.mathworks.com/")

#Wait time
time.sleep(3)

#locate and click button
button = driver.find_element(By.LINK_TEXT, "Explore MATLAB")
button.click()

#Wait time
time.sleep(5)

#Close browser
driver.quit()


