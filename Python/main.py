from function import *

url = {
        'path':'https://apis.openapi.sk.com/tmap/routes/pedestrian',
        'poi':'https://apis.openapi.sk.com/tmap/pois'
        }

tkey = mkKey()

endP = findEndPoint(url, tkey)
checkDirect(endP, url, tkey)


