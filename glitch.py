#Import Statements Needed For Program
from selenium import webdriver
import time

#Website for Editing Bot Page
url = "https://glitch.com/edit/#!/insta-bot-akini?path=index.html%3A5%3A6"
driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
driver.get(url)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/main/div/section[4]/div[2]/article/div/div[1]/textarea ").send_keys("Hello")

