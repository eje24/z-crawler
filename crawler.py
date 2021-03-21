from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.mitrecsports.com/')
time.sleep(100)
