from selenium import webdriver
import time
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


driver = webdriver.Chrome('./chromedriver')

# first load into mit rec sports
driver.get('http://www.mitrecsports.com/')

driver.implicitly_wait(5)

#click login button
login_page_link = driver.find_element_by_id('menu-item-647').find_element_by_tag_name('a')
print(login_page_link.get_attribute('text'))
login_page_link.click()

#enter login information
username_input = driver.find_element_by_id('ctl00_pageContentHolder_loginControl_UserName')
password_input = driver.find_element_by_id('ctl00_pageContentHolder_loginControl_Password')
username = os.environ['ACC_USERNAME']
password = os.environ['ACC_PASSWORD']
username_input.send_keys(username)
password_input.send_keys(password)
driver.implicitly_wait(3)
login_button = driver.find_element_by_id('ctl00_pageContentHolder_loginControl_Login')
login_button.click()