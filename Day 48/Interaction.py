from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

"""GETTING A PIECE OF TEXT"""
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
# article_count.click()

"""GETTING A PIECE OF TEXT BY LINK AND CLICKING THE LINK"""
# article = driver.find_element(By.LINK_TEXT, "Talk")
# article.click()

"""FINDING SEARCH AND ENTERING SEARCH CONTENT"""
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)