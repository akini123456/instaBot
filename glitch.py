#Import Statements Needed For Program
import time
from selenium import webdriver
import random

#Status Variables
forever = True

while forever:
    for x in range(1, 60):
        time.sleep(1)
        print(x)
    url = ["https://youtu.be/4sXXJRxGFhs", "https://youtu.be/aWYIDoh89es"]
    driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
    driver.get(url[1])
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button").click()
    for x in range(1, 46):
        time.sleep(1)
        print(x)
    driver.close()
