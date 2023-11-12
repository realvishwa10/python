# Automatic job application

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "ghostyyyyyghost@gmail.com"
PASS = "ghostyghost10"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3716911744&f_AL=true&f_WT=2&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[4]/a[1]').click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASS)

driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

driver.find_element(By.CLASS_NAME, 'jobs-save-button').click()