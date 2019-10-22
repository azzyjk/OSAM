from function import *
import time

url = {
        'path':'https://apis.openapi.sk.com/tmap/routes/pedestrian',
        'poi':'https://apis.openapi.sk.com/tmap/pois'
        }

tkey = mkKey()

#목적지 주소 입력받기
endP = findEndPoint(url, tkey)

while True:
    dicts=getLocate()
    dicts.update(endP)
    checkDirect(dicts, url, tkey)
    time.sleep(1)
