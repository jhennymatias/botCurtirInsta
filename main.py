from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
             
    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(5)
        user = self.driver.find_element_by_name('username')
        user.send_keys(self.username)
        time.sleep(5)
        senha = self.driver.find_element_by_name('password')
        senha.send_keys(self.password)
        senha.send_keys(Keys.RETURN)
        time.sleep(5)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/sombriosc/')         
        time.sleep(3)
        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

insta = instaBot('user', 'senha')
insta.Login()
insta.curtir_fotos()