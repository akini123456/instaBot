#Import Statements Needed For Program
from selenium import webdriver
import time

#Log information
googleUsername = 'aryankini@gmail.com'
googlePassword = 'Sony70big1'

#Forms Website
url = "https://gmail.com"

#Open Browser and Open Up Forms
driver = webdriver.Chrome('C:/Users/aryan/Downloads/chromedriver.exe')
driver.get(url)

#Put Email Address
driver.find_element_by_id('identifierId').send_keys(googleUsername)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
