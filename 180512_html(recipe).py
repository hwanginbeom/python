import requests
from bs4 import BeautifulSoup

url = 'http://board.miznet.daum.net/gaia/do/cook/recipe/mizr/read?articleId=16329&&bbsId=MC001&pageIndex=1'
for page in range (1):
    params = {
        'start': (page-1)*10,
        }

    response = requests.get(url, params=params)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select(('dd[class*=stuff]'))
 
    for idx, title in enumerate(title_list, 1):
        print(title.text)
