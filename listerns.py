from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
import time

# Custom listener class
class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(f"Finding element by {by} with value {value}")

    def after_find(self, by, value, driver):
        print(f"Element found by {by} with value {value}")

# Initialize WebDriver (assuming ChromeDriver is in PATH)
driver = webdriver.Chrome()
driver.maximize_window()

# Wrap the WebDriver instance with EventFiringWebDriver
event_driver = EventFiringWebDriver(driver, MyListener())

# Navigate to Wikipedia page
event_driver.get("https://en.m.wikipedia.org/wiki/List_of_national_capitals_by_population")

# Wait for the table to load (you can add explicit wait if needed)
time.sleep(3)

# Step 3: Extract table data
table = event_driver.find_element(By.XPATH, "//table[@class='wikitable sortable mw-datatable sticky-header static-row-numbers sort-under col1left col2left jquery-tablesorter']")
rows = table.find_elements(By.TAG_NAME, "tr")

table_data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    cols_data = []
    for col in cols:
        cols_data.append(col.text)
    table_data.append(cols_data)

# Print table data
for data in table_data:
    print(data)

# Close the browser
event_driver.quit()
