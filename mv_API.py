import random
import requests
import xml.etree.ElementTree as ET
from time import sleep
import itertools

def get_data(data):  # 사용자가 입력한 정보를 영화 포스터로 반환하는 함수
    new_data = []
    value_set = [
        {"1": "드라마", # 로맨스 → 드라마
         "2": "코메디", # 코미디 → 코메디
         "3": "액션",
         "4": "공포"},

        {"1": [2016, 2018],
         "2": [2011, 2015],
         "3": [2006, 2010],
         "4": [2000, 2006]},

        {"1": "돈",
         "2": "로봇",
         "3": "동물",
         "4": "총"},

        {"1": "도시",
         "2": "시골",
         "3": "집",    # 산 → 집
         "4": "호텔"}, # 절 → 호텔

        {"1": "잠",
         "2": "노래",
         "3": "음식",
         "4": "바다"},

        {"1": "10대",
         "2": "20대",
         "3": "30대",
         "4": "40대"},

        {"1": "대한민국",
         "2": "미국",
         "3": "일본",
         "4": "대한민국"}] # 프랑스 → 대한민국

    for i in range(len(data)):
        new_data.append(value_set[i][data[i]])
        
    # 검색에 필요한 데이터 준비
    genre = new_data[0]
    year = new_data[1]
    plot = ','.join([new_data[2], new_data[3], new_data[4]])
    nation = new_data[6]

    # API CALL & 결과 파싱
    res = call_api(genre, year, plot, nation)
    xtree = ET.fromstring(res.text)
    rows = xtree.find("Result").findall("Row")
    rowsLength = len(rows)
    # 만약 데이터가 없으면
    if rowsLength == 0:  # plot 2개 첫번째 조합
        plot = ','.join([new_data[2],new_data[3]]) 
        res = call_api(genre, year, plot, nation)
        xtree = ET.fromstring(res.text)
        rows = xtree.find("Result").findall("Row")
        rowsLength = len(rows)
        
        if rowsLength == 0: # plot 2개 두번째 조합
          plot = ','.join([new_data[2],new_data[4]])
          res = call_api(genre, year, plot, nation)
          xtree = ET.fromstring(res.text)
          rows = xtree.find("Result").findall("Row")
          rowsLength = len(rows)

          if rowsLength == 0: # plot 2개 세번째 조합
              plot = ','.join([new_data[3],new_data[4]])
              res = call_api(genre, year, plot, nation)
              xtree = ET.fromstring(res.text)
              rows = xtree.find("Result").findall("Row")
              rowsLength = len(rows)
              
              if rowsLength == 0: # plot 1개씩 조회
                for i in range(2, 5):
                    plot = new_data[i]
                    res = call_api(genre, year, plot, nation)
                    xtree = ET.fromstring(res.text)
                    rows = xtree.find("Result").findall("Row")
                    rowsLength = len(rows)
                    if rowsLength != 0:
                        break

    try:
      randomIndex = random.randrange(0, rowsLength)
      poster = rows[randomIndex].find('posters')
      return poster.text.split("|")[0]

    except: # 총 1.3% 에러 발생 확인 = 장르 - 공포
      poster = "https://post-phinf.pstatic.net/MjAxNzEwMTJfNyAg/MDAxNTA3NzczNzEzNDE4.4If6TI_4nn5ChT26Fz0i8oiLwCk_npOfvhMM2DGzI0Mg.IESbtvY3N2vmNK8o3JQU347ph2h6cVJ7bR74gV7JOLcg.JPEG/%EC%8F%981.jpg?type=w1200" # 쏘우 포스터
      return poster
      pass

def call_api(genre, year, plot, nation):
    # API URI 준비
    callURI = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_xml2.jsp?collection=kmdb_new2&detail=Y&ServiceKey=GD2S7LJMI3FZ3035F6M9'  # 기본 URI
    callURI += f'&genre={genre}'  # 장르
    callURI += f'&releaseDts={year[0]}0101'  # 시작개봉날짜
    callURI += f'&releaseDte={year[1]}1231'  # 끝개봉날짜
    callURI += f'&plot={plot}'  # 줄거리
    callURI += f'&nation={nation}'

    # API CALL
    print(callURI)
    res = requests.get(callURI)
    return res


# 디버그 확인 함수
# import itertools
# event = list(itertools.product([1,2,3,4], repeat=7))
# for i in event:
#   get_data(i)

# 국가-일본일때 에러 COUNT = 139/4096 = 3% 
# 국가-일본에서 미국 에러 COUNT = 52/4096 = 1.3%