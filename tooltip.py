import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (choose the appropriate WebDriver for your browser)
driver = webdriver.Chrome()


# Navigate to the webpage containing the element with a tooltip
driver.get("https://admin-demo.nopcommerce.com/")
time.sleep(1)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
time.sleep(1)
driver.find_element(By.ID,"Password").clear()
time.sleep(2)
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@class='nav-link']//i[@class='nav-icon fas fa-tags']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[@class='nav-item']//p[contains(text(),' Discounts')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='SearchDiscountName']").send_keys("'20% order total' discount")

time.sleep(2)
driver.find_element(By.XPATH,"(//i[@class='fas fa-search'])[2]").click()
time.sleep(2)
text=driver.find_elements(By.XPATH,"//table[@id='discounts-grid']/tbody/tr/td[1]")
time.sleep(2)
for i in text:
   assert i.text=="'20% order total' discount"






# Close the browser window
driver.quit()
