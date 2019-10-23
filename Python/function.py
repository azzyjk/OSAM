import requests
import json
import os
import serial

#apikey값 가져오기
def mkKey():
    key = open('C:\\Users\\Admin\\Desktop\\OSAM\\txtfiles\\tmapKey.txt', 'r')
    return key.read()

#지도 누른 곳 위도&경도 가져오기
def getLocate():
    read = open('C:\\Users\\Admin\\Desktop\\OSAM\\txtfiles\\location.txt', mode='rt', encoding='utf-8')
    lonlat=read.readline().split(',')
    dicts = {
            'startX':lonlat[1],
            'startY':lonlat[0]
            }
    return dicts
    
#POI검색 파라미터 만들기
def poiPara(address, key):
	params = {'version':'1', 
            'count':'6',
            'searchKeyword':address, 
            'appKey':key
            }
	return params

#길찾기 파라미터 만들기
def pthPara(dicts ,key):
    params = { 'version':'1',
                'appKey':key,
                'startX':dicts['startX'], 
                'startY':dicts['startY'], 
                'endX':dicts['endX'], 
                'endY':dicts['endY'],
                'startName':'출발지',
                'endName':'도착지'
            }
    return params
    
#방향 알려주기
def notice(direct):
    arduino = serial.Serial('COM7', 9600)
    val=None;
    if direct==12 or direct==212:
        val='l'
    elif direct==13 or direct==213:
        val='r'
    elif direct==201:
        print('end')
    else:
        val='s'
    a=a.encode('utf-8')
    arduino.write(a)

#다음 가야할 방향 찾기
def checkDirect(dicts, url ,key):
    params=pthPara(dicts, key)
    res = requests.post(url['path'],data=params)
    for i in res.json()['features'] :
        check = "turnType" in i['properties']
        if(check==True and i['properties']['turnType'] !=200):  #출발지 분류 코드 넘어가기
            direct = i['properties']['turnType']
            notice(direct)
            break


#POI검색 후 선택한 위치 정보 반환
def search(url, param):
    res = requests.get(url['poi'], params=param)
    number = 0
    for i in res.json()['searchPoiInfo']['pois']['poi']:
        print("%d. " %number, i['name'])
        number+=1

    choose = input("번호를 선택해주세요 : ")
    return res.json()['searchPoiInfo']['pois']['poi'][int(choose)]

#목적지검색 후 목적지의 위도, 경도 반환
def findEndPoint(url, key):
    os.system("cls")
    endPt = input("목적지를 입력해 주세요 : ")
    
    params = poiPara(endPt, key)
    res = search(url, params)
    
    os.system("cls")

    dicts = {'endX':res['frontLon'],
            'endY':res['frontLat']
            }
            
    return dicts
    
def locateTracking(end,url, key):
    dicts=getLocate()
    dicts.update(end)
    checkDirect(dicts, url, key)
    
