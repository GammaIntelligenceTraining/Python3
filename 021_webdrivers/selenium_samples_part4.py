from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Specify browser driver location
driver_location = "chromedriver.exe"

# Connect browser driver
driver = webdriver.Chrome(driver_location)

# Will put driver to wait mode for 5 seconds
driver.implicitly_wait(5)

# get() command will open browser and visit page given in ()
driver.get('https://particle-clicker.web.cern.ch/')

click_object = driver.find_element_by_id('detector-events')

actions = ActionChains(driver)
actions.click(click_object)
count = 0

for i in range(500):
    actions.perform()
    count += 1
    print(count)