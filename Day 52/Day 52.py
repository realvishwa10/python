from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\\Users\\Vishwa\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
SIMILAR_ACCOUNT = "leomessi"
USERNAME = "ghosty_ghosttt"
PASS = "ghostyghost10"


class InstaFollowerBot:

    def __init__(self, driver_path):
        service = Service(executable_path=driver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.url = "https://www.instagram.com"

    def log_in(self):
        self.driver.get(f"{self.url}/accounts/login/")
        time.sleep(3)
        self.driver.maximize_window()
        uname = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        uname.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASS)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"{self.url}/{SIMILAR_ACCOUNT}")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/article/header/div[2]/ul/li[2]/a/span")
        followers.click()
        time.sleep(2)
        pop_up_scroll = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_scroll)
            time.sleep(2)

    def follow(self):
        pass


bot = InstaFollowerBot(CHROME_DRIVER_PATH)
bot.log_in()
bot.find_followers()
bot.follow()