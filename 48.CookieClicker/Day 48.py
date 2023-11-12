from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Woodland-2812118sa_Khaki_6-Leather-Boots-6-2812118SAKHAKI/dp/B081LPPTLW/ref=sr_1_19?keywords=boots+for+men&qid=1695602876&refinements=p_89%3AWoodland&rnid=3837712031&s=shoes&sr=1-19")

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print(price)

driver.quit()