using python selenium
  
from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with the path to your ChromeDriver
driver = webdriver.Chrome("path/to/chromedriver")

# Navigate to the Instagram profile URL
driver.get("https://www.instagram.com/guviofficial/")

# Follower count XPATH (relative)
follower_count_xpath = ".//*[@title='Followers']/span"
follower_count = driver.find_element(By.XPATH, follower_count_xpath).text

# Following count XPATH (relative)
following_count_xpath = ".//*[@title='Following']/span"
following_count = driver.find_element(By.XPATH, following_count_xpath).text

# Print the extracted follower and following count
print("Followers:", follower_count)
print("Following:", following_count)

driver.quit()
