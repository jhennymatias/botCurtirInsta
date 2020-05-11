from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

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
        self.curtir_fotos('araranguasc')
        
        
    def curtir_fotos(self, hashtag, likes = 20):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')         
        time.sleep(3)
        driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
        item = 1
        while item <= likes: # loop with how many photos to like
            try:
                time.sleep(2)
                driver.find_element_by_class_name('fr66n').click() # click the like button
                time.sleep(random.randint(40, 70)) # break time between likes and comment due to instagram policy against bots
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
                item = item + 1
            except:
                time.sleep(60)
                
        print(f'Number of photos liked: \033[0;33m{item - 1}\033[m')
        
def main():
    user = input("Digite o usuario: ")
    senha = input("Digite a senha: ")
    insta = instaBot(user, senha)
    insta.Login()

if __name__ == "__main__":
    main()