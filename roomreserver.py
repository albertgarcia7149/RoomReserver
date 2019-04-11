from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
import time

url="chromedriver.exe"
driver=webdriver.Chrome(url)


page_url = 'https://calendar.library.ucsc.edu/booking/seu'

day = "18";
day_of_week = "Thursday"
month = "April"
year = "2019"
location = "S&E308 (4)"
time_start = "8:00am"
time_end = "9:00am"

driver.get(page_url)

#Select the calender
calender=driver.find_element_by_xpath("/html/body/div[3]/div[2]/section/div/div/div[2]/div[1]/div[3]/div/div/table")
#Click on the day you want in the calender
calender.find_element_by_link_text(day).click()

time.sleep(2)

#Select the room schedule table
table=driver.find_element_by_xpath('//*[@id="s-lc-rm-right"]')
#Click the time square
table.find_element_by_xpath("//a[@title='S&E308 (4), 8:00am to 8:30am, Thursday, April 18, 2019']").click()


# driver.close()
# driver.quit()
