import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%95%84%EC%8B%9C%EC%95%88%EA%B2%8C%EC%9E%84+%EB%A9%94%EB%8B%AC%EC%88%9C%EC%9C%84"
res=requests.get(url)
bs4=BeautifulSoup(res.content, 'html.parser')

print(res) # 된건지 확인
a = bs4.select('#main_pack > div.sc.cs_asian_game._cs_asian_game > div.asian_game_content > div.asian_game_wrap > div.medal_ranking > div > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.name.top > a.nation_name')

