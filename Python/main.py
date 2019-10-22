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
    locateTracking(endP, url, tkey)
    time.sleep(1)

