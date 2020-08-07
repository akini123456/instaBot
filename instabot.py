#Import Statements Needed For Program
from selenium import webdriver
import time
import random

#Status Variables
instaOpen = False
forever = True

#User information
username = "engagestemeastbrunswick"
password = "engagestemeb421"

#URL for Website
url = "https://www.instagram.com/"
while forever:
    time.sleep(180)
    #Open Browser and Open Up Instragram
    try:
        driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
        driver.get(url)
        instaOpen = True
    except:
        print("Chromedriver Failure")

    if(instaOpen):
        #Log into Instrgram
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username) #username
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password) #password
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click() #Log in Button

        #Auto-Login Denied
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        except:
            print("That option doesn't exsist")

        #No Notifications
        driver.implicitly_wait(5)
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        except:
            print("That option doesn't exsist")

        #See All New Reccomendation
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()

        #Follow People
        driver.implicitly_wait(7.5)
        for x in range(1, 11):
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[" + str(x) + "]/div[3]/button").click()
            driver.implicitly_wait(random.randint(8,16))
        time.sleep(1)
        driver.close()
