def mkKey():
    key = open('C:\\Users\\Admin\\Desktop\\OSAM\\txtfiles\\tmapKey.txt', 'r')
    return key.read()
    
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