import random
import requests
import xml.etree.ElementTree as ET

import datetime
def getYesterday(): 
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday

def get_data():  # 사용자가 입력한 정보를 반환하는 함수
    # API CALL & 결과 파싱
    res = call_boxapi(today)
    xtree = ET.fromstring(res.text)
    rows = xtree.find("Result").findall("Row")
    rowsLength = len(rows)


    randomIndex = random.randrange(0, rowsLength)
    boxdate = rows[randomIndex].find('rank','rankOldAndNew','movieNm','audiCnt')
    return boxdate.text.split("|")[0]


def call_boxapi(today):
    # API URI 준비
    callboxURI = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f449386f024e1c05ff8f6b4d486d54cc&itemPerPage=10'
# 기본 URI
    callboxURI += f'&targetDt={today}'  #오늘날짜

    # API CALL
print(callboxURI)

