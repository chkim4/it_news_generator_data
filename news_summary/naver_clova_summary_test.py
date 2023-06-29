"""
네이버 Clova 문서요약 테스트
"""
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()
X_NCP_APIGW_API_KEY_ID = os.environ.get("X-NCP-APIGW-API-KEY-ID")
X_NCP_APIGW_API_KEY = os.environ.get("X-NCP-APIGW-API-KEY")

# 요청에 필요한 url, 헤더, 데이터 
URL = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"

headers = {'Content-Type': 'application/json',
           'X-NCP-APIGW-API-KEY-ID': X_NCP_APIGW_API_KEY_ID,
           'X-NCP-APIGW-API-KEY': X_NCP_APIGW_API_KEY}

data = {'document':{'content': ''}, 'option': {'language': 'ko', 'model': 'news'}}

# 요약할 기사 임의로 크롤링
browser=webdriver.Chrome()
browser.get('https://n.news.naver.com/mnews/article/215/0001109625?sid=105')

soup=BeautifulSoup(browser.page_source, "html.parser")
div = soup.find_all('div', {'id': 'dic_area'})

# 크롤링한 뉴스 기사를 body에 추가
data['document']['content'] = div[0].get_text().strip()

# 요청
r = requests.post(url = URL, headers=headers, data= json.dumps(data)) 

result = r.json()

print(result)