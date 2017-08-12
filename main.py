import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

f = open('password', 'r')

driver = webdriver.Chrome("D:/Downloads/chromedriver.exe")
driver.get("https://buzzport.gatech.edu/")
driver.implicitly_wait(5000)
login_button = driver.find_element_by_name('login_btn')
login_button.click()
driver.implicitly_wait(5000)
driver.find_element_by_name('username').send_keys('ali74')
driver.find_element_by_name('password').send_keys(f.readline())
driver.find_element_by_name('submit').click()
driver.implicitly_wait(5000)
driver.find_element_by_xpath("//img[@src='https://buzzport.gatech.edu/site/images/lock_48x48.gif']").click()
driver.implicitly_wait(5000)

driver.get('https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin')
driver.implicitly_wait(5000)
driver.find_element_by_xpath("//input[@value='Submit']").click()