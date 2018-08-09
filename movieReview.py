import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import xml.etree.ElementTree as ET
import re
import os

def get_request_url(url,enc = 'utf-8'): # url을 얻어오는 부분 
    # utf-8 의 형태로 받는다 .

    req=urllib.request.Request(url) # url을 얻어온다. 

    try:
        response=urllib.request.urlopen(req) # url을 열고 
        if response.getcode() ==200: # 코드가 정상일 때 
            try:
                rcv=response.read() # 연것을 읽고 
                ret=rcv.decode(enc) # ??
            except UnicodeDecodeError:
                ret=rcv.decode(enc,'replace') # 오류났을 때 대체한다 

            return ret

    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.tatetime.now(),url))
        return None

def getPelicanaAddress(result):  #

    movie_index='167697'
    for i in movie_index:
        Movie_URL='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=%s&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false' %str(movie_index)

        rcv_data=get_request_url(Movie_URL)
        soupData=BeautifulSoup(rcv_data,'html.parser')

        movie_div=soupData.find('div',attrs={'class':'score_result' })
        ul = movie_div.find('ul')
        lis=ul.findAll('li')
        
        bEnd=True
        for i in lis:
            score=i.find('div',class_="star_reple").find('em').get_text()
            spectator=i.find('div',class_="score_people").find('span').get_text()
            review=i.find('div',class_="score_score").find('p').get_text()

            result.append(review)
            #result2.append([score])

            
        print(result)
        if(bEnd==True):
            return
    return

def main():

    result=[]

    print('PERICANA ADDRESS CRAWLING START')
    getPelicanaAddress(result)
    print(result)
    pericana_table=pd.DataFrame(result,columns=('store','sido','gungu','store_address'))
    pericana_table.to_csv("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python36\\pericana.csv",encoding="cp949",mode='w',index=True)
    del result[:]

if __name__=='__main__':
    main()
