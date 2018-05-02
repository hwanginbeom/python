import requests
from bs4 import BeautifulSoup

url = 'https://www.yelp.com/search?find_loc=Paris,+France&sortby=review_count&cflt=restaurants'
for page in range (1,101):
    params = {
        'start': (page-1)*10,
        }

    response = requests.get(url, params=params)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select(('span[class*=review-count]'))
 
    for idx, title in enumerate(title_list, 1):
        print(title.text)
   
