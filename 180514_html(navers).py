from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3) 
driver.get('https://www.go.com/') 
driver.find_element_by_name('query').send_keys('L’As du Fallafel')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()

html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
elem = soup.select('#sp_blog_1 > dl > dt > a.sh_blog_title')
print(elem)
