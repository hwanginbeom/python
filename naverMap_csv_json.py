import sys
import urllib.request
import datetime
import time
import json
import folium
import pandas as pd
import csv

def get_request_url(url) :
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-id", 'XbJnzQczJf1XGQxWYHPU')
    req.add_header("X-Naver-Client-Secret",'3GXFZKRTyn')
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
def getGeoData(address):
    
    base = "https://openapi.naver.com/v1/map/geocode"
    node = ""
    parameters = "?query=%s" % urllib.parse.quote(address)
    url = base + node + parameters
    
    retData = get_request_url(url)
    
    if (retData == None) :
        return None
    else : 
        return json.loads(retData)

#geo_path='../data/pericana.csv'
#geo_str=json.load(open(geo_path,encoding='utf-8'))
#geo_data=geo_str,
csvfile=open('pericana.csv','r')
jsonfile=open('pericana.json','w')
fieldnames = ("index","store","sido","gungu","store_Address")

reader = csv.DictReader(csvfile, fieldnames)

for row in reader:

    json.dump(row, jsonfile, ensure_ascii=False)

    jsonfile.write('\n')




jsonResult = getGeoData('충청북도 청주시 흥덕구 풍산로 103(복대동)')



if 'result' in jsonResult.keys():
    print('검색어', jsonResult['result']['userquery'])
    
    for item in jsonResult['result']['items']:
        print('==================')
        print('주소 : ', item['address'])
        print('위도 : ', str(item['point']['y']))
        print('경도 : ', str(item['point']['x']))
        
map_osm = folium.Map(location = [item['point']['y'], item['point']['x']], zoom_start=13)

folium.Marker([item['point']['y'], item['point']['x']]).add_to(map_osm)
map_osm
