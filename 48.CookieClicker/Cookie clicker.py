from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get cookie
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item list
upgrade_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute(name="ID") for item in upgrade_items]

# Set timers
timeout = time.time() + 5
five_mins = time.time() + (60 * 5)

while True:
    cookie.click()

    if time.time() > timeout:
        # Get all items price - SPLITTING IS DIFFICULT HERE
        price_list = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # prices = [item.text for item in price_list]
        # print(prices)

        # Keep prices alone in a list
        prices = []
        for price in price_list:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)

        # Dictionary of store items and their prices
        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[prices[n]]= item_ids[n]

        # Our wallet
        money_text = driver.find_element(By.ID, "money").text
        if "," in money_text:
            money_text = money_text.replace(",", "")
        money = int(money_text)

        # Find affordable upgrades
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        if len(affordable_upgrades) > 0:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time()+5

    if time.time() >= five_mins:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break
