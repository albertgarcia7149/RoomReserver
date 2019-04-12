from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import os
import time

url="chromedriver.exe"
driver=webdriver.Chrome(url)


first_name = "Albert"
last_name = "Garcia"
email = "awgarcia@ucsc.edu"
group_name = "Python Bravo"

page_url = 'https://calendar.library.ucsc.edu/booking/sel'

day = "18";
day_of_week = "Thursday"
month = "April"
location = "S&E135 (5)"

driver.get(page_url)

#Select the calender
#calender=driver.find_element_by_xpath("/html/body/div[3]/div[2]/section/div/div/div[2]/div[1]/div[2]/div/div/table")
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

continue_button = driver.find_element_by_xpath('//*[@id="rm_tc_cont"]')
continue_button.click()

fname_box = driver.find_element_by_xpath('//*[@id="fname"]')
fname_box.send_keys(first_name)

lname_box = driver.find_element_by_xpath('//*[@id="lname"]')
lname_box.send_keys(last_name)

email_box = driver.find_element_by_xpath('//*[@id="email"]')
email_box.send_keys(email)

group_box = driver.find_element_by_xpath('//*[@id="nick"]')
group_box.send_keys(group_name)

status_drop = Select(driver.find_element_by_id("q1"))
status_drop.select_by_index(1)

purpose_drop = Select(driver.find_element_by_id("q2"))
purpose_drop.select_by_index(3)

submit_button = driver.find_element_by_id('s-lc-rm-sub')
submit_button.click()
