import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/s?k=phone&crid=2MC9DYRY6LCFV&sprefix=PHO%2Caps%2C213&ref=nb_sb_ss_ts-doa-p_2_3")
wait=WebDriverWait(driver,10)
main_window = driver.current_window_handle
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='a-section aok-relative s-image-fixed-height'][1]"))).click()
time.sleep(10)

t=driver.window_handles
for i in t:

       driver.switch_to.window(i)
       print(driver.title)

