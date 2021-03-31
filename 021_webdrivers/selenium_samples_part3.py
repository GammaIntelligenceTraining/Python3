from selenium import webdriver
# Will import methods that allow usage of keys like Enter, Esc etc.
from selenium.webdriver.common.keys import Keys
import time

driver_location = "chromedriver.exe"

# Connect browser driver
driver = webdriver.Chrome(driver_location)

# get() command will open browser and visit page given in ()
driver.get('https://gammatest.net')

link = driver.find_element_by_link_text('Rohkem infot')
# link = driver.find_element_by_xpath('//*[@id="hp"]/div[1]/div[3]/div[1]/p[2]/a')
link.click()

# A for loop to get all elements from page
element = driver.find_elements_by_tag_name('td')
for piece in element:
    print(piece.text)


time.sleep(3)
# Will go one page back
driver.back()

time.sleep(3)
# Will go one page forward
driver.forward()


russian = driver.find_element_by_link_text('На русском')
russian.click()

element = driver.find_elements_by_tag_name('td')
for piece in element:
    print(piece.text)