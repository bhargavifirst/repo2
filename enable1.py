import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Amazon page
driver.get("https://www.firstcry.com/toys-and-gaming/5/0/0?sort=bestseller&ref2=menu_dd_catlanding")

try:

     driver.find_element(By.XPATH, "//span[@class='sprite_list sprt'][1]").click()
     time.sleep(10)
     title=driver.title
     print(title)

except:
    print("exception")

driver.quit()
