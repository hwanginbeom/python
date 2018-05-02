import requests
from bs4 import BeautifulSoup

url = 'https://www.yelp.com/search?find_loc=paris&cflt=restaurants'
for page in range (1,101):
    params = {
        'start': (page-1)*10,
        }

    response = requests.get(url, params=params)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select('h3.search-result-title > span[class*=indexed-biz-name]')
 
    for idx, title in enumerate(title_list, 1):
        print(title.text)
   
