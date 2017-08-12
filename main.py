import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

courses = [90068,89622,90243]
while True:
    current_time = time.clock()
    driver = webdriver.Chrome("D:/Downloads/chromedriver.exe")
    driver.get("https://buzzport.gatech.edu/")
    driver.implicitly_wait(10)
    login_button = driver.find_element_by_name('login_btn')
    login_button.click()
    driver.find_element_by_name('username').send_keys('ali74')
    driver.find_element_by_name('password').send_keys(open('password', 'r').readline())
    driver.find_element_by_name('submit').click()
    driver.find_element_by_xpath("//img[@src='https://buzzport.gatech.edu/site/images/lock_48x48.gif']").click()
    driver.get('https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin')
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(1)
    while time.clock() < current_time + 1800:
        for course in courses:
            driver.find_element_by_id('crn_id1').send_keys(course)
            driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
            try:
                driver.find_element_by_id('waitaction_id1').click()
                driver.find_element_by_xpath("//option[@value='WL']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
            except:
                print 'waitlist full'
            time.sleep(2)
        time.sleep(10)