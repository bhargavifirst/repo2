import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_4bzeat7dnl_e&adgrpid=1326012680679100&hvadid=82876055443053&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=116072&hvtargid=kwd-82876733542853:loc-90&hydadcr=5619_2377285&msclkid=6a3e284ef66a117bd9564ef77351ea84")
element=driver.find_element(By.ID,"searchDropdownBox")
ele=driver.find_element(By.XPATH,"//span[text()='Hello, sign in']")
a=ActionChains(driver)
s = Select(element)
s.select_by_visible_text("Electronics")
time.sleep(5)
a.move_to_element(ele).perform()
time.sleep(5)