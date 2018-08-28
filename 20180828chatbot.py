import requests
import os
from bs4 import BeautifulSoup
#1.api 사용 기본 url 설정 
#vi ~/.bashrc 해서 bashrc 설정 파일을 열어서
#export chbot_TOKEN=token
#:wq
#$env | grep chatbot_TOKEN


token = os.getenv('chatbot_TOKEN')
base_url= "https://api.telegram.org/bot{}/".format(token)

#2. chat id 를 받아오는 코드
# ~~~~~/getUpdates 요청을 보내고 ,
#json에서 chat_id 값을 뽑아 오면 됩니다.
res = requests.get(base_url+"getUpdates").json() #자동으로 딕셔너리로 만든다.
chat_id=res['result'][0]['message']['from']['id']

#3. 크롤링 
res = requests.get('https://finance.naver.com/sise/')
result=BeautifulSoup(res.content , 'html.parser')
kospi = result.select_one('#KOSPI_now')


msg = kospi.text
msg_url = "sendMessage?chat_id={}&text={}".format(chat_id,msg)
requests.get(base_url+msg_url)
