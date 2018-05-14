
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.kr/maps/place/LasduFallafel/@48.8573825,2.3569738,17z/data=!3m1!4b1!4m5!3m4!1s0x47e66e025d19942f:0x710304a633dfc4c2!8m2!3d48.857379!4d2.3591625'
for page in range (1):
    params = {
        'start': (page-1)*10,
        }

    response = requests.get(url, params=params)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select(('ul.section-rating-term-list'))
 
    for idx, title in enumerate(title_list, 1):
        print(title.text)
