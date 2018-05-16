from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.google.co.kr')

test=["L’As du Fallafel","kong"]
a=0
driver.find_element_by_name('q').send_keys(test[a]) 
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').submit()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')
elem = driver.find_element_by_xpath('//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div').text


print(elem)
