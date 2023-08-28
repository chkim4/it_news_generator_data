"""
네이버 Clova 문서요약 테스트

n개의 추출 요약만 가능
"""
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
X_NCP_APIGW_API_KEY_ID = os.environ.get("X-NCP-APIGW-API-KEY-ID")
X_NCP_APIGW_API_KEY = os.environ.get("X-NCP-APIGW-API-KEY")

def clova_summary(content: str) -> str:
    """
    clova의 문서 요약 기능 호출. \n

    매개변수: \n
    content -- 요약에 사용할 원문 기사 (str) \n

    \n   

    반환: \n
    result -- content를 추출 요약 3문장으로 요약한 결과 (str)
    """

    # 요청에 필요한 url, 헤더, 데이터 
    URL = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"

    headers = {'Content-Type': 'application/json',
            'X-NCP-APIGW-API-KEY-ID': X_NCP_APIGW_API_KEY_ID,
            'X-NCP-APIGW-API-KEY': X_NCP_APIGW_API_KEY}

    data = {'document':{'content': content}, 'option': {'language': 'ko', 'model': 'news'}}

    # 요청
    r = requests.post(url = URL, headers=headers, data= json.dumps(data)) 
    result = r.json()

    return result['summary']