import random

def get_data(data): # 사용자가 입력한 정보를 list 형태로 반환하는 함수
  new_data = []

  value_set = [
      {"1" : "로맨스",
        "2" : "코미디",
        "3" : "액션",
        "4" : "공포",
        "5" : "SF"},

       {"1" : random.randrange(2016,2021),
        "2" : random.randrange(2011,2016),
        "3" : random.randrange(2006,2011),
        "4" : random.randrange(2000,2006)},

      {"1" : "돈",
        "2" : "로봇",
        "3" : "동물",
        "4" : "총"},
      
      {"1" : "도시",
        "2" : "시골",
        "3" : "산",
        "4" : "절"},
      
       {"1" : "잠",
        "2" : "노래",
        "3" : "음식",
        "4" : "바다"},
      
       {"1" : "10대",
        "2" : "20대",
        "3" : "30대",
        "4" : "40대"}, 
      
       {"1" : "한국",
        "2" : "미국",
        "3" : "일본",
        "4" : "프랑스"}]

  for i in range(len(data)):
     new_data.append(value_set[i][data[i]])
  print(new_data)

# audiAcc	누적관람인원 : 50만원