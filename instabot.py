# Import Statements Needed For Program
import time
from selenium import webdriver

# Status Variables
forever = True

# Username and Password
username = "eb_stemandbuds"
password = "MGGZ10585"

# Instagram URL
url = "https://instagram.com"

while True:
    # Waits 180 seconds
    for x in range(1, 181):
        time.sleep(1)
        print(x)

    # Opens Instagram
    driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
    driver.get(url)
    time.sleep(1)

    # Log into Instagram
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    time.sleep(3)

    # No auto log in
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(1.5)

    # No notifications
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(1.5)

    # See all recommendations
    driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
    time.sleep(1.5)

    # Friend people
    for x in range(1, 9):
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div["+ str(x) +"]/div[3]/button").click()
        time.sleep(0.8)

    # Waits 5 secs
    time.sleep(5)

    # Close Chrome
    driver.close()