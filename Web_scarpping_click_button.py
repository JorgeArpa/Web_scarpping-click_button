
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


browser=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver_win32 (1)\chromedriver.exe')
# browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver_win32\chromedriver.exe')
url='https://transparency.entsoe.eu/load-domain/r2/yearLoad/show'
browser.get(url)
#time.sleep(5)
browser.find_element_by_xpath(
            ".//*[contains(text(), 'I Agree')]"
        ).click()

elem=browser.find_elements_by_xpath(
            "//*[@class='dv-filter-hierarchic-wrapper']"
        )
print(elem)

for i in range(10):
    try:
        browser.find_element_by_xpath(
            "//*[@class='dv-filter-hierarchic-wrapper']"
        ).click()
        
    except NoSuchElementException as e:
        print('retry in 1s.')
        time.sleep(1)
else:
    raise e