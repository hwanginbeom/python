import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/sise/'
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
a = result.select_one('#KOSPI_now')
b = result.select('#KOSPI_now')
print(a)
print(b)
c = result.select_one('#KOSPI_now')# 하나는 <class 'bs4.element.Tag'> 이 형태로 온다 
d = result.select('#KOSPI_now')[0]# 이게 하나는 list형식이고 
print(type(c))
print(c.text)
print(d.text)
#BeautifulSoup 를 통해 이 소스를 조절한다.

#KOSPI_now
#content
