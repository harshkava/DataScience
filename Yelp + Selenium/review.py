# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:16:45 2018

@author: Harsh Kava
"""
"""
The script implements 4 functions:

- login(username,password): This function uses selenium to login to Yelp.

- submitReview(rev_text, rev_rating, restaurantID): this function submits a review for the restaurant with id restaurantID.
 The parameter rev_text is the review's text. 
 The parameter rev_rating is the review's star rating.
 The user has to be logged in before this function is called.

- vote(userID): this  function goes to the Yelp profile of the user with id=userID, and marks the first review  (the one at the top of the page) as "useful".
  The user has to be logged in before this function is called. 

- run(username,password,rev_text, rev_rating, restaurantID, userID): This function calls and tests the other 3 functions.
   Use the Yelp account details like userId & password.
"""

#Note: I have added sleep time between & inside methods so that you can see the actions getting carried out at a slower pace.
#we can remove this sleep intervals if required.

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('chromedriver.exe',desired_capabilities=dcap,service_args=service_args)

def login(username,password):
    #access website
    driver.get('https://www.yelp.com/')
    
    #find and click login icon
    icon=driver.find_element_by_xpath('//*[@id="header-log-in"]/a')
    icon.click()
    
	#Accessing Login frame
    form=driver.find_element_by_id('ajax-login')
    form.click()
    
	#Entering email details
    email = form.find_element_by_id('email')
    email.send_keys(username)
    time.sleep(2)
	
	#Entering password details
    pwd = form.find_element_by_id('password')
    pwd.send_keys(password)
    time.sleep(2)
	
	#Clicking the login button
    button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajax-login"]/button')))
    button.click()

def submitReview(rev_text,rev_rating, restaurantID):
    time.sleep(2)  
    
	#find and click the login 
    write_review=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'write-review')))
    write_review.click()
    time.sleep(2)  
    
	#for searching a particular restaurant
	rest = driver.find_element_by_id("war_desc")
    rest.send_keys(restaurantID)
    
    rest = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div/div[1]/form/div/div[2]/button')
    rest.click()
    time.sleep(2)  
	
    icon1=driver.find_element_by_xpath('//*[@id="super-container"]/div/div/div[1]/ul/li[1]/div/div[1]/div/div[2]/a[2]')
    icon1.click()
    time.sleep(2) 
		
	#Entering review for particular restaurant
    finding=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/form/div[1]/div/textarea')))
    finding.send_keys(rev_text)
    time.sleep(1)
	
    icon=driver.find_element_by_id('rating-'+rev_rating)
    icon.click()
    
    time.sleep(2)                                                                            
    button=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[2]/button')))
    button.click()
    #time.sleep(3)
    
   
def vote(userID):
    #find and click the userID
    driver.get('https://www.yelp.com/user_details?userid='+userID)
    time.sleep(2) 
    #find and click the useful 
    usefulbutton =  driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div/div[1]/div/div/ul/li[1]/div/div[2]/div[2]/div[1]/ul/li[1]/a')
    usefulbutton.click()
     
#main method to call other methods    
def run(username,password,rev_text, rev_rating, restaurantID, userID):
   
    login(username,password)
    time.sleep(2)
    submitReview(rev_text, rev_rating, restaurantID)
    time.sleep(2)
    vote(userID)

#Note: Enter some userid and password in run() method
# Fill the 1st '' with Yelp Id and 2nd '' with password to run this program.

run('','','this is so good','1','Coal Fire','XdOpoFiTBVMbUhYBRfpYzQ')
