import time
import datetime
import os

from selenium import webdriver
from datetime import timedelta
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

#click on reservation box
driver.implicitly_wait(3)
reservation_box = driver.find_element_by_id('menu_SCH')
reservation_box.click()

#click on Fitness Reservations box
driver.implicitly_wait(3)
fitness_reservation_box = driver.find_element_by_xpath('//div[@title="Fitness Reservations"]')
fitness_reservation_box.click()

#directed to new page with a single Fitness Reservations box -- need to click time as well
driver.implicitly_wait(3)
fitness_reservation_box = driver.find_element_by_xpath('//div[@title="Fitness Reservations"]')
fitness_reservation_box.click()

#select the next day on the popup
driver.implicitly_wait(3)
calendar_img = driver.find_element_by_xpath('//img[@class="ui-datepicker-trigger"]')
calendar_img.click()
reservation_day = datetime.date.today() + timedelta(days=1)
month = reservation_day.month - 1

day_of_week = reservation_day.ctime().split()[0]
print(month)

#continue_popup_button = driver.find_element_by_id('btnContinue')
#continue_popup_button.click()
