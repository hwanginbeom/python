import os
import sys
import urllib.request
import datetime
import time
import json
from itertools import count
import pandas as pd
def get_save_path():  # 패스를 저장해주는 함수
    save_path = "C:\\parser\RoadData.csv"
    # 저장할 위치와 파일명 적기
    save_path = save_path.replace("\\", "/")
    # /이게 있을경우 파이썬 에서 쓰는 \\ 의 형태로 만들어서 경로를 지정해준다.

    if not os.path.isdir(os.path.split(save_path)[0]):
        # 만약 이폴더가 없을경우 새로 생성해주는 그런 것 같다 이건 찾아 봐야 알 듯
        os.mkdir(os.path.split(save_path)[0])

    return save_path

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 1]

def getGeoData(lat,lng):
    base = "https://api2.sktelecom.com/tmap/road/nearToRoad?version=1"
    appkey = "&appKey=ec633e08-ce42-48a8-9674-a3e09c7bea73"
    #lat = lat.encode('utf-8')
    #lng = lng.encode('utf-8')
    parameters = "&lat=%s"%(lat)+"&lon=%s"%(lng)
    url = base + appkey + parameters
    print(url)
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def writeData(jsonResult,lat,lng):
    f = open(get_save_path(), 'a', encoding="euc-kr")
    if jsonResult==None:
        return None

    elif 'resultData' in jsonResult.keys():
        # print('총 결과: ',jsonResult['resultData'])
        try:
            f.write(jsonResult['resultData']['header']['linkId'] + ",")  # 링크아이디
            f.write(jsonResult['resultData']['header']['roadName'] + ",")  # 도로이름
            f.write(str(jsonResult['resultData']['linkPoints'][0]['location']['latitude']) + ",")  # 시점위도
            f.write(str(jsonResult['resultData']['linkPoints'][0]['location']['longitude']) + ",")  # 시점경도
            f.write(str(jsonResult['resultData']['linkPoints'][1]['location']['latitude']) + ",")  # 종점위도
            f.write(str(jsonResult['resultData']['linkPoints'][1]['location']['longitude']) + ",")  # 종점경도
            f.write(str(jsonResult['resultData']['header']['speed']) + ",")  # 도로제한속도
            f.write(str(jsonResult['resultData']['header']['roadCategory']) + ",")  # 도로분류 원도로등급  (0:고속국도, 1:도시고속화도로, 2:국도, 3;국가지원지방도, 4:지방도, 5:주요도로 1, 6:주요도로 2, 7:주요도로 3, 8:기타도로 1, 9:이면도로, 10:페리항로, 11:단지내도로, 12 :이면도로 2(세도로))
            f.write(lat+",")
            f.write(lng+"\n")
        except Exception as e:
            print(e)
            return None


def main():
    carAccident_in_Korea = pd.read_csv("C:\\parser\CarAccident_Korea_since_2012.csv", thousands=',',encoding='utf-8')
    idx=12500
    while True:

        bEnd = True
        lat = carAccident_in_Korea.iloc[idx]['위도']
        lng = carAccident_in_Korea.iloc[idx]['경도']
        print(lat)
        lat = float(lat)
        lng = float(lng)
        idx += 1
        if carAccident_in_Korea['위도'].all()>0:
            bEnd = False
            lat = str(lat)
            lng = str(lng)
            jsonResult = getGeoData(lat, lng)
            print(idx,"번째 크롤링:")
            print(jsonResult,lat,lng)
            writeData(jsonResult,lat,lng)

        if bEnd == True:
            return
        if idx==25040:
            return



if __name__ == '__main__':
    main()
