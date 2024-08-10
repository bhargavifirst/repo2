from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://en.m.wikipedia.org/wiki/List_of_national_capitals_by_population")
ele={}
ele=driver.find_element(By.XPATH,"//table[@class='wikitable sortable mw-datatable sticky-header static-row-numbers sort-under col1left col2left jquery-tablesorter']").text
print(ele)
