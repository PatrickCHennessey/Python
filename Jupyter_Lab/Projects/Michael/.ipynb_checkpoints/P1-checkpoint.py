# Using Selenium this script will open up the BBC website and navigate to the page containing defined text

from time import sleep

from selenium.webdriver import Chrome

driver = Chrome()

driver.get('https://www.bbc.co.uk')

t = driver.title

element = driver.find_element_by_partial_link_text('12 of the best films to watch in November') # Used partial as copying the text provided extra blocks

element.click()

print(t)

sleep(60)