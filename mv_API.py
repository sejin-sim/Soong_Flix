import random
import requests
import xml.etree.ElementTree as ET


def get_data(data):  # 사용자가 입력한 정보를 영화 포스터로 반환하는 함수
    new_data = []
    value_set = [
        {"1": "로맨스",
         "2": "코미디",
         "3": "액션",
         "4": "공포",
         "5": "SF"},

        {"1": random.randrange(2016, 2018),
         "2": random.randrange(2011, 2016),
         "3": random.randrange(2006, 2011),
         "4": random.randrange(2000, 2006)},

        {"1": "돈",
         "2": "로봇",
         "3": "동물",
         "4": "총"},

        {"1": "도시",
         "2": "시골",
         "3": "산",
         "4": "절"},

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
         "4": "프랑스"}]

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
    if rowsLength == 0:
        # plot 값을 변경해가며 실행
        for i in range(2, 5):
            plot = new_data[i]
            res = call_api(genre, year, plot, nation)
            xtree = ET.fromstring(res.text)
            rows = xtree.find("Result").findall("Row")
            rowsLength = len(rows)
            if rowsLength != 0:
                break

    randomIndex = random.randrange(0, rowsLength)
    poster = rows[randomIndex].find('posters')
    print(poster)
    return poster.text.split("|")[0]


# audiAcc	누적관람인원 : 50만원

def call_api(genre, year, plot, nation):
    # API URI 준비
    callURI = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_xml2.jsp?collection=kmdb_new2&detail=Y&ServiceKey=GD2S7LJMI3FZ3035F6M9'  # 기본 URI
    callURI += f'&genre={genre}'  # 장르
    callURI += f'&releaseDts={year}0101'  # 시작개봉날짜
    callURI += f'&releaseDte={year}1231'  # 끝개봉날짜
    # callURI += f'&releaseDts=20100101'  # 시작개봉날짜
    # callURI += f'&releaseDte=20201231'  # 끝개봉날짜
    callURI += f'&plot={plot}'  # 줄거리
    callURI += f'&nation={nation}'

    # API CALL
    print(callURI)
    res = requests.get(callURI)
    return res
