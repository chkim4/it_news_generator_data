"""
kakao koGPT 문서요약 API 호출

1문장의 생성 요약만 가능
"""
import requests
import json
import os
import dotenv

dotenv.load_dotenv()
KAKAO_REST_API_KEY = os.environ.get("KAKAO-REST-API-KEY")

# KoGPT API 호출을 위한 메소드
def kogpt_summary(content: str, max_tokens = 1800, temperature = 0.1, top_p = 0.1, n = 1) -> str:
    """
    kogpt의 문서 생성 요약 기능 호출. \n

    매개변수: \n
    content -- 요약에 사용할 원문 기사 (String) \n
    나머지 -- kogpt에서 요청하는 값. 자세한 건 api 문서 참고. 값은 문장 요약하면서 가장 나은 값으로 설정 \n
    https://developers.kakao.com/docs/latest/ko/kogpt/rest-api#sample-text-summary
    
    \n
    
    반환: \n
    result -- content를 생성 요약 1문장으로 생성 요약한 결과 (String) \n
    """
    prompt = content + '\n 한줄 요약:' 
    
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',

        headers = {
            'Authorization': 'KakaoAK ' + KAKAO_REST_API_KEY,
            'Content-Type': 'application/json'
        }, 

        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        }
    )
    
    # 응답을 JSON 형식으로 변환
    result = json.loads(r.content)

    return result['generations'][0]['text']