"""
날짜 : 2021/06/07
이름 : 김승용
내용 : 파이썬 전국 날씨 데이터 크롤링 실습
"""
import os

import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

response = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
# print(response.text)

# 페이지 파싱
dom = bs(response.text, 'html.parser')
trs = dom.select('#weather_table > tbody > tr')

# 디렉터리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    # 해당 디렉터리가 존재하지 않으면
    os.makedirs(dir)

# 데이터 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 데이터 파일 저장
file.write('지역,현재일기,시정,운량,중하운량,현재기온,이슬점온도,불쾌지수,일강수,습도,풍향,풍속,해면기압\n')

for i, tr in enumerate(trs):
    tds = tr.find_all('td')
    file.write("{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(tds[0].text,
                                                               tds[1].text,
                                                               tds[2].text,
                                                               tds[3].text,
                                                               tds[4].text,
                                                               tds[5].text,
                                                               tds[6].text,
                                                               tds[7].text,
                                                               tds[8].text,
                                                               tds[9].text,
                                                               tds[10].text,
                                                               tds[11].text,
                                                               tds[12].text))

# 파일 닫기
file.close()
print('날씨 데이터 수집 완료..')