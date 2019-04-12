from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import os
import sys
import time

# Define webdriver location and initialize webdriver
url="chromedriver.exe"
driver=webdriver.Chrome(url)

# Define user information to fill out form
first_name = "Albert"
last_name = "Garcia"
email = "awgarcia@ucsc.edu"
group_name = "Python Bravo"

# Get command line args for date of booking
if len(sys.argv) != 4:
    print("Usage: Day_of_week Month Day (ex: Thursday April 18")
    exit()

# Define the page we will look on to make the booking
# This is set up for S&E lower floor room 135
page_url = 'https://calendar.library.ucsc.edu/booking/sel'
location = "S&E135 (5)"

# Assign command line args
day = sys.argv[3];
day_of_week = sys.argv[1]
month = sys.argv[2]

driver.get(page_url)

#Select the calender
calender=driver.find_element_by_xpath('//*[@id="s-lc-rm-cal"]')
#Click on the day you want in the calender
calender.find_element_by_link_text(day).click()

time.sleep(1)

#Select the room schedule table
table=driver.find_element_by_xpath('//*[@id="s-lc-rm-right"]')

#Query example
#'S&E308 (4), 3:00pm to 3:30pm, Thursday, April 18, 2019'

query1= location + ', 3:00pm to 3:30pm, ' + day_of_week + ', '+ month + ' ' + day + ', 2019'
query1 = "//a[@title='"+ query1+ "']"

query2= location + ', 3:30pm to 4:00pm, ' + day_of_week + ', '+ month + ' ' + day + ', 2019'
query2 = "//a[@title='"+ query2+ "']"

query3= location + ', 4:00pm to 4:30pm, ' + day_of_week + ', '+ month + ' ' + day + ', 2019'
query3 = "//a[@title='"+ query3+ "']"

query4= location + ', 4:30pm to 5:00pm, ' + day_of_week + ', '+ month + ' ' + day + ', 2019'
query4 = "//a[@title='"+ query4+ "']"

try:
    #Click the time square
    table.find_element_by_xpath(query1).click()
    table.find_element_by_xpath(query2).click()
    table.find_element_by_xpath(query3).click()
    table.find_element_by_xpath(query4).click()

except NoSuchElementException:
    print("Time slot not avaliable")
    driver.close()
    driver.quit()

time.sleep(1)
#Press continue button to open form
continue_button = driver.find_element_by_xpath('//*[@id="rm_tc_cont"]')
continue_button.click()
#Enter first name
fname_box = driver.find_element_by_xpath('//*[@id="fname"]')
fname_box.send_keys(first_name)
#Enter last name
lname_box = driver.find_element_by_xpath('//*[@id="lname"]')
lname_box.send_keys(last_name)
#Enter email
email_box = driver.find_element_by_xpath('//*[@id="email"]')
email_box.send_keys(email)
#Enter group name
group_box = driver.find_element_by_xpath('//*[@id="nick"]')
group_box.send_keys(group_name)
# Select undergrad
status_drop = Select(driver.find_element_by_id("q1"))
status_drop.select_by_index(1)
# Select class project
purpose_drop = Select(driver.find_element_by_id("q2"))
purpose_drop.select_by_index(3)
# Submit
submit_button = driver.find_element_by_id('s-lc-rm-sub')
submit_button.click()
