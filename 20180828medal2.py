import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%95%84%EC%8B%9C%EC%95%88%EA%B2%8C%EC%9E%84+%EB%A9%94%EB%8B%AC%EC%88%9C%EC%9C%84"
res=requests.get(url)
bs4=BeautifulSoup(res.content, 'html.parser')

print(res) # 된건지 확인

name = bs4.select_one('a.nation_name')
nation_names =bs4.select('a.nation_name')
nation_names_f =bs4.find('a.nation_name')

for nation in nation_names:
    print(nation.text)

gold = bs4.select('td.gold')
for count in gold :
    print(count.text)
type(nation_names)
type(nation_names_f)

dir(nation_names)
#모 할수 있는지

####통째로 가져오기
 
tables = bs4.select('.ranking_list') # 테이블을 통째로 가져온다.

tables.count
len(tables) #가져올게 2개인데 2개 맞는지 

for col in tables:
    for row in col.select('tbody > tr'):
        print(row.select_one('a.nation_name').text)
        print(row.select_one('td.gold').text) # select('td.gold')[0].text 이건 리스트로 들어오고 select_one은 bs4 어쩌고로 나온다 그래서 바로 출력가능 
        print(row.select_one('td.silver').text)
        print(row.select_one('td.bronze').text)
