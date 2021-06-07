"""
날짜 : 2021/06/07
이름 : 김승용
내용 : 파이썬 HTML 페이지 Parsing 실습하기

파싱(Parsing)
 - 문서 해독을 의미
 - 마크업 문서(HTML, XML)에서 특정 태그의 데이터를 추출하는 처리 과정
"""

import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청
response = req.get('https://news.naver.com/',
                   headers={'User-Agent': 'Mozilla/5.0'})

# print(response.text)

# 페이지 파싱
dom = bs(response.text, 'html.parser')
titles = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
# print(titles)

# 파싱 데이터 출력(strip() : 공백 제거)
# for tit in titles:
#     print(tit.text.strip())

# 다음 뉴스 랭킹 1~10 출력하기
res = req.get('https://news.daum.net/ranking/popular',
              headers = {'User-Agent': 'Mozilla/5.0'})

# 페이지 파싱
dom2 = bs(res.text, 'html.parser')
titles2 = dom2.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

# 파싱 데이터 출력(strip() : 공백제거)
for i in range(10):
    print(titles2[i].text)
