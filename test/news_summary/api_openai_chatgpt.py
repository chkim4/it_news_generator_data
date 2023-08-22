"""
ChatGPT 문서요약 API 호출 \n

1문장의 생성 요약으로 설정
"""
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI-API-KEY")
FULL_OPENAI_API_KEY = "Bearer " + OPENAI_API_KEY

def chatgpt_summary(content: str) -> str:
    """
    매개변수: \n
    content -- 요약에 사용할 원문 기사 

    \n

    반환: \n
    result -- content를 생성 요약 1문장으로 요약한 결과 (String)
    """
    
    content_prefix = "Summarize the following article in 1 setences in Korean: "
    full_content = content_prefix + content
    
    # 요청에 필요한 url, 헤더, 데이터 
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",

        headers = {
            'Authorization': FULL_OPENAI_API_KEY, 
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }, 
        json = {
            'model': 'gpt-3.5-turbo-0613',
            'messages': [{'role': "user", 'content': full_content}]
        }
    )
    r.encoding = 'utf-8'
    result = json.loads(r.text)

    return result['choices'][0]['message']['content']

