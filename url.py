import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com")

wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.ID,"nav-search-submit-button"))).click()
time.sleep(10)