"""
Created on Mon Apr  1 13:16:45 2018

@author: Harsh Kava
"""
"""
-The purpose of this script is to scrape data from dynamic website like Trip Advisor:
# It finds all the restaurants in the first page and print their names

"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#set emailId & Password to log in to tripadvisor.com
emailId = ''    # Ex: '*******@mail.com'
password = ''				# Ex: 'as8df79hkjA'

#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('chromedriver.exe',desired_capabilities=dcap,service_args=service_args)

#access website
driver.get('https://www.tripadvisor.com/')

#find and click login icon
icon=driver.find_element_by_xpath('//*[@id="taplc_global_nav_action_profile_0"]/div/a[1]/span')
icon.click()

#find and switch to the popup frame
popup=driver.find_element_by_id('overlayRegFrame')
driver.switch_to.frame(popup)
time.sleep(1)

#find and fill the email box
email=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'regSignIn.email')))
email.send_keys(emailId)

#find and fill the password box
pswd=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'regSignIn.password')))
pswd.send_keys(password)

#find and click the login button
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regSignIn"]/div[3]')))
button.click()

#find and click the Restaurants button
myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'global-nav-restaurants')))

el=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'global-nav-restaurants')))
el.click()

#find and fill the search box
#searchBox=driver.find_element_by_class_name('typeahead_input')
searchBox=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'typeahead_input')))
searchBox.send_keys('Hoboken')

#find and click the search button
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'SUBMIT_RESTAURANTS')))
button.click()

#wait until the page loads
myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'property_title')))


els=driver.find_elements_by_class_name('property_title')
for el in els:
    print (el.text)


