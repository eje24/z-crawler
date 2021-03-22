from selenium import webdriver
import time
import datetime
import os

from preferences import SLOT_PREFERENCES
from selenium import webdriver
from datetime import timedelta
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


driver = webdriver.Chrome('./chromedriver')

def get_reservation_day():
    reservation_day = datetime.date.today() + timedelta(days=1)
    day = reservation_day.day
    [day_of_week, month] = reservation_day.ctime().split()[:2]
    return (month, day, day_of_week)

def navigate_to_available_slots():
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
    #every once and a while takes too long to load and next thing isn't found
    calendar_img = driver.find_element_by_xpath('//img[@class="ui-datepicker-trigger"]')
    calendar_img.click()

    (month, day, day_of_week) = get_reservation_day()


    month_dropdown = driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
    month_dropdown.click()

    for option in month_dropdown.find_elements_by_tag_name('option'):
        if option.text == month:
            option.click()

    month_dropdown.click()

    calendar = driver.find_element_by_xpath('//table[@class="ui-datepicker-calendar"]')
    for calendar_days in calendar.find_elements_by_tag_name('a'):
        if calendar_days.text == str(day):
            calendar_days.click()

    continue_popup_button = driver.find_element_by_id('btnContinue')
    continue_popup_button.click()

    # access available reservation slots 
    time.sleep(5)
    select_all = driver.find_element_by_id('ancSchSelectAll')
    select_all.click()

    duration = driver.find_element_by_id('ctl00_pageContentHolder_lstDuration').find_element_by_tag_name('option')
    duration.click()

    search = driver.find_element_by_id('ancSchSearch')
    search.click()

    list_view = driver.find_element_by_id('ctl00_pageContentHolder_OLSLabel2')
    list_view.click()

SLOT_TO_TIME = ['7:00','8:45','10:30','12:15','2:30','4:15','6:00','7:45']

def get_preferences():
    """
    Returns timeslots associated with current reservation day, in order of priority
    """
    week_day = get_reservation_day()[2]
    slot_list = list(map(lambda day: SLOT_TO_TIME[day], SLOT_PREFERENCES[week_day]))
    return slot_list

def search_available_slots(preferences):
    pass

def main():
    navigate_to_available_slots()
    preferences = get_preferences()
    print(preferences)
    search_available_slots(preferences)

if __name__ == '__main__':
    main()
