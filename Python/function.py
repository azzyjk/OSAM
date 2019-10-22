import requests
import json
import os

#apikey값 가져오기
def mkKey():
    key = open('C:\\Users\\Admin\\Desktop\\OSAM\\txtfiles\\tmapKey.txt', 'r')
    return key.read()

#POI검색 파라미터 만들기
def poiPara(address, key):
	params = {'version':'1', 
            'count':'6',
            'searchKeyword':address, 
            'appKey':key
            }
	return params

#길찾기 파라미터 만들기
def pthPara(key):
    params = { 'version':'1',
                'appKey':key,
                'startX':'126.972580', 
                'startY':'37.409999', 
                'endX':'126.972620', 
                'endY':'37.409746',
                'startName':'%EC%B6%9C%EB%B0%9C',
                'endName':'%EB%B3%B8%EC%82%AC'
            }
    return params
    
#방향 알려주기
def notice(direct):
    if direct==12 or direct==212:
        print('left')
    elif direct==13 or direct==213:
        print('right')
    elif direct==16 or direct==214:
        print('8시')
    elif direct==17 or direct==215:
        print('10시')
    elif direct==18 or direct==216:
        print('2시')
    elif direct==19 or direct==217:
        print('4시')

#다음 가야할 방향 알아내기
def checkDirect(url ,key):
    params=pthPara(key)
    res = requests.post(url['path'],data=params)
    for i in res.json()['features'] :
        check = "turnType" in i['properties']
        if(check==True and i['properties']['turnType'] !=200):
            direct = i['properties']['turnType']
            print(direct)
            notice(direct)
            break



#POI검색
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
    endX = res['frontLon']
    endY = res['frontLat']
    lists = [endX, endY]
    return lists
    