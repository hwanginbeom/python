from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(3) 
driver.get('https://www.google.co.kr/search?ei=L0P5WqH2D4b-8gXJnKegDA&q=L%E2%80%99As+du+Fallafel') 
driver.clear()
driver.find_element_by_name('q').send_keys('L’As du Fallafel')

html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
elem = soup.select('#sp_blog_1 > dl > dt > a.sh_blog_title')
print(elem)
