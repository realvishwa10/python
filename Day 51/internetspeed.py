from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\\Users\\Vishwa\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
TWITTER_EMAIL = "ghostyyyyyghost@gmail.com"
TWITTER_PASS = "ghostyghost10"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        service = Service(executable_path=driver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.DOWN = f"down: {self.down}"
        print(self.DOWN)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.UP = f"up: {self.up}"
        print(self.UP)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        time.sleep(3)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASS)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        log_in.click()
        time.sleep(3)
        tweet_bar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_bar.send_keys(f"{self.UP}\n{self.DOWN}\nPromised Up: {PROMISED_UP}\nPromised Down: {PROMISED_DOWN}\nwhy am i paying for 150 mbps and getting only {self.UP}")
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()