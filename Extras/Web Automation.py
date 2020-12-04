#Dependencies
#	selenium

#	Command: pip install selenium




from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser= webdriver.Chrome()

browser.get("http://www.onefivenine.com/busRoute.dont?method=loadBusRoutesFinder")

resultSet = browser.find_element_by_id("tabmenu");

options = resultSet.find_elements_by_tag_name("li")


options[0].click()


select = Select(browser.find_element_by_id('cityId'))
# select by value 
select.select_by_value('6759')

select = Select(browser.find_element_by_id('stageId'))
# select by value 
select.select_by_value('11772')

data=browser.find_element_by_id("findBusStages");

print(data.text, end='\n')
