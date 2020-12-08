import requests
import json
import datetime as dt
import pandas as pd
import numpy as np
from pandas import DataFrame
from matplotlib import pyplot

def box():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    session = requests.Session()
    session.headers.update( {'User-agent': user_agent, 'referer': None} )

    #어제날짜
    
    
    today=dt.datetime.now()
    delta=dt.timedelta(days=-1)
    yesterday=today+delta
    date = str(yesterday)
    date = date[:10]
    yesterday_str= str(yesterday).replace("-","")
    yesterday_str = yesterday_str[:8]
    #호출에 사용할 API
    callboxURI = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f449386f024e1c05ff8f6b4d486d54cc&itemPerPage=10&targetDt='+yesterday_str

    #json 활용
    r = session.get(callboxURI)
    r.encoding = "utf-8"
    r.text

    #json을 딕셔너리로 변환
    daily_boxoffice_dict = json.loads(r.text)

    daily_boxoffice_df = DataFrame(daily_boxoffice_dict['boxOfficeResult']['dailyBoxOfficeList'])

    # 딕셔너리 내에서 활용 할 값 추출
    tmp_df = daily_boxoffice_df.filter(['rank','movieNm','openDt','audiAcc'])
    
    tmp_df['audiAcc'] = pd.to_numeric(tmp_df['audiAcc'])
    tmp_df.update(tmp_df.select_dtypes(include=np.number).applymap('{:,}'.format))
    
    Boxoffice = list((tmp_df.values.tolist()))
    return Boxoffice