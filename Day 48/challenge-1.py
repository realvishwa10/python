from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(events_dates)):
    events[n] = {
        "date": events_dates[n].text,
        "name": events_names[n].text
    }

print(events)
driver.quit()
