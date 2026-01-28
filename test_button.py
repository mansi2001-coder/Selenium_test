from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("https://in.mathworks.com/")

# Step 3: Wait for page to load
time.sleep(3)

# Step 4: Find button and click
button = driver.find_element(By.LINK_TEXT, "Explore MATLAB")
button.click()

# Step 5: Wait to see result
time.sleep(5)

# Step 6: Close browser
driver.quit()
