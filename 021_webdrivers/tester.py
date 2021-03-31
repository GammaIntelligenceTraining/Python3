from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('https://cv.ee/et/')

location = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div[3]/form/div[1]/div/div[1]/div/div/div[1]/div[1]/div[1]/span')
location.click()

input_field = driver.find_element_by_xpath('//*[@id="react-select-2-input"]')
input_field.send_keys('Tallinn')
input_field.send_keys(Keys.TAB)
time.sleep(5)

topic = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div/div/div[3]/form/div[1]/div/div[3]/div/div/div[1]/div[1]/span')
topic.click()

input_field_topic = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div[3]/form/div[1]/div/div[3]/div/div/div[1]/div[2]/div/input')
input_field_topic.send_keys('Python')
input_field.send_keys(Keys.TAB)

ok_button = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div/div/div[3]/form/div[3]/footer/span/button/span')
ok_button.click()