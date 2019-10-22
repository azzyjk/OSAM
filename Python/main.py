from function import *
import requests
import json
import pprint

url = 'https://apis.openapi.sk.com/tmap/routes/pedestrian'

tkey = mkKey()

params = pthPara(tkey)

res = requests.post(url, data=params)

pprint.PrettyPrinter(indent=4).pprint(res.json())
