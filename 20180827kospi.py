import requests
from bs4 import BeautifulSoup
res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
kospi = soup.select('#KOSPI_now')
print(kospi)
