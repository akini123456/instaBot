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
    for x in range(1, 181):
        time.sleep(1)
        print(x)
    print("-----------------------------------------------------------------------------------------------------------")
    #Open Browser and Open Up Instragram
    try:
        driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
        driver.get(url)
        instaOpen = True
        print("Instagram Bot Online")
    except:
        print("Chromedriver Failure")
    if(instaOpen):
        #Log into Instrgram
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username) #username
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password) #password
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click() #Log in Button

        #Auto-Login Denied
        driver.implicitly_wait(15)
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
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/button").click()
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button[2]").click()
            print("Instagram found out im a bot")
            print("Shut down for 10 minutes starts now!")
            driver.close()
            for x in range(1, 601):
                time.sleep(1)
                print(x)
        except:
            #Follow People
            driver.implicitly_wait(7.5)
            for x in range(2, 9):
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[" + str(x) + "]/div[3]/button").click()
                    driver.implicitly_wait(random.randint(8,16))
                except:
                    print("No More Suggestions Available")
            print("-----------------------------------------------------------------------------------------------------------")
            print("People were friended")
            print("Task was done")
            print("-----------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            driver.close()
