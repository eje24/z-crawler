from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.mitrecsports.com/')

driver.implicitly_wait(5)
login_link = driver.find_element_by_id('menu-item-647').find_element_by_tag_name('a')
print(login_link.get_attribute('text'))
login_link.click()
