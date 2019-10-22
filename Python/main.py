from function import *

url = {
        'path':'https://apis.openapi.sk.com/tmap/routes/pedestrian',
        'poi':'https://apis.openapi.sk.com/tmap/pois'
        }

tkey = mkKey()

address = input("검색할 지명을 입력해 주세요 : ")

res = search(url, poiPara(address, tkey))

print(res)
