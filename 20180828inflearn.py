import requests
from bs4 import BeautifulSoup

url='https://search.onoffmix.com/event?c=85'
#요청을 보낼 주소를 가져온다
res=requests.get(url)
#2.그 주소로요청을 보낸다. 
print(res)
#res.status_code=> 200 이면 값은 성공적으로 가져 왔다는 것
#3.원하는 값을 찾는다. 
#print(res.content)
#페이지 소스보기 
print(res.url)
result=BeautifulSoup(res.content , 'html.parser')
a = result.select_one('#content > div > div.sideLeft > div.contentBox.todayEventArea > ul:nth-child(133) > li.eventTitle')

#course-list > li.course_single_item.course_id_177843.course_status_publish.course_author_20183 > div > div.col-md-8.col-sm-8 > div > div.item-title > a
#course-list > li.course_single_item.course_id_182835.course_status_publish.course_author_17 > div > div.col-md-8.col-sm-8 > div > div.item-title > a
print(a.text)
#BeautifulSoup 를 통해 이 소스를 조절한다.

#KOSPI_now
#content
