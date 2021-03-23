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

def get_reservation_date():
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
    time.sleep(1)
    fitness_reservation_box = driver.find_element_by_xpath('//div[@title="Fitness Reservations"]')
    fitness_reservation_box.click()

    #directed to new page with a single Fitness Reservations box -- need to click time as well
    driver.implicitly_wait(3)
    time.sleep(1)
    fitness_reservation_box = driver.find_element_by_xpath('//div[@title="Fitness Reservations"]')
    fitness_reservation_box.click()

    #select the next day on the popup
    #every once and a while takes too long to load and next thing isn't found
    time.sleep(2)
    calendar_img = driver.find_element_by_xpath('//img[@class="ui-datepicker-trigger"]')
    calendar_img.click()

    (month, day, day_of_week) = get_reservation_date()


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

SLOT_TO_TIME = [['07:00 AM','08:45 AM','10:30 AM','12:15 PM','02:30 PM','04:15 PM','06:00 PM','07:45 PM'], ['10:15 AM', '12:00 PM', '02:00 PM', '03:45 PM', '05:30 PM']]
WEEK_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

def get_preferences(week_day):
    """
    Returns timeslots associated with current weekday, in order of priority
    """
    weekend = 0 if week_day in WEEK_DAYS else 1
    slot_list = list(map(lambda day: SLOT_TO_TIME[weekend][day], SLOT_PREFERENCES[week_day]))
    return slot_list

def get_next_page():
    """
    Finds and clicks next page button
    """
    next_button = driver.find_element_by_id('ancSchListNext')
    next_button.click()

def get_prev_page():
    """
    Finds and clicks previous page button
    """
    prev_button = driver.find_element_by_id('ancSchListPrevious')
    prev_button.click()

def next_page_exists():
    """
    Checks whether or not current page is equal to the last page
    """
    driver.implicitly_wait(15)
    page_number_span = driver.find_element_by_id('PageNumber')
    page_number_text = page_number_span.find_element_by_tag_name('span').text
    left = page_number_text[5:page_number_text.find('o')-1]
    right = page_number_text[page_number_text.find('f')+2:]
    return left != right

def prev_page_exists():
    """
    Checks whether or not previous page exists
    """
    driver.implicitly_wait(15)
    page_number_span = driver.find_element_by_id('PageNumber')
    page_number_text = page_number_span.find_element_by_tag_name('span').text
    left = page_number_text[5:page_number_text.find('o')-1]
    return left != '1'


def search_current_page(slot_time):
    slot_table_div = driver.find_element_by_id('schPageData')
    driver.implicitly_wait(5)
    available_slot_list = slot_table_div.find_elements_by_xpath('//tbody/tr')
    for slot_element in available_slot_list:
        if slot_element.get_attribute('class') not in  {'DgText', 'DgTextAlt'}:
            continue
        #print(slot_element.get_attribute('class'))
        current_row = slot_element.find_elements_by_tag_name('td')
        if current_row[0].text == slot_time:
            return current_row[-1].find_element_by_tag_name('a')
        # print(slot_element.find_element_by_xpath('/td').text)
    return None

def find_slot(slot_time):
    driver.implicitly_wait(5)
    search_current_page(slot_time)
    while next_page_exists():
        result = search_current_page(slot_time)
        if result != None:
            return result
        get_next_page()
    return None

def return_to_start():
    """
    Clicks previous until it returns to start page
    """
    while prev_page_exists():
        get_prev_page()
    

def search_available_slots(desired_slots):
    for slot_time in desired_slots:
        print("attempting to find:", slot_time)
        #attempt to find slot
        result = find_slot(slot_time)
        if result != None:
            print("Found desired slot!!")
            result.click()
            schedule_slot()
            return True
        #if not, navigate back to first page to try again for next slot
        return_to_start()
    return False

def schedule_slot():
    time.sleep(2)
    continue_button = driver.find_element_by_id('btnContinue')
    continue_button.click()

    driver.implicitly_wait(3)
    accept_waiver = driver.find_element_by_id('btnAcceptWaiver')
    accept_waiver.click()
    
def main():
    navigate_to_available_slots()
    reservation_day = get_reservation_date()[2]
    desired_slots = get_preferences(reservation_day)
    print("Today's preferences are: ", desired_slots)
    if not search_available_slots(desired_slots):
        print("No slots found...")


if __name__ == '__main__':
    main()
