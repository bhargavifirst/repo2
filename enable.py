import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver, 10)
driver.get("https://api.cogmento.com/register/")
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
time.sleep(5)
b= driver.find_element(By.XPATH, "//input[@id='terms']").is_selected()
print(b)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
c=driver.find_element(By.XPATH, "//input[@id='terms']").is_selected()
print(c)
time.sleep(5)


