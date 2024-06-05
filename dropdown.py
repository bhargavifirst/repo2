import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")
time.sleep(3)
str = driver.current_url
print("url" + str)
a="sahiti"
b="aashvi"
print(a+b)
driver.maximize_window()
ele = driver.find_element(By.ID,"searchDropdownBox")
time.sleep(3)

drp = Select(ele)#we have to pass element as a parameter
for i in drp.options:


    drp.select_by_visible_text(i.text)

time.sleep(3)

driver.find_element(By.ID,"nav-search-submit-button").click()
mouse = driver.find_element(By.XPATH,"//span[@class='nav-icon nav-arrow'][1]")
action=ActionChains(driver)#we have to passd driver as a parameter

action.move_to_element(mouse).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//*[text()='TE'][1]").click()
time.sleep(2)

