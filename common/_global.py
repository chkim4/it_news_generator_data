"""
공통 함수, 전역 변수 등
"""

def convert_crawl_to_dict(full_text: str, url: str, ord: int) -> dict:
    """
    크롤링한 뉴스 기사를 DB에 저장할 때 필요한 dict 형태로 변환 \n
    230824 - 현재는 네이버 뉴스만 크롤링하지만, 추후 다른 사이트 크롤링을 고려하여 공통 함수를 별도 분리. \n

    매개변수: \n
    full_text -- 기사 본문 (str) \n
    url -- 기사 URL (str) \n
    ord -- 오늘 전체 기사 중 해당 기사의 순번 (str) \n

    \n
    
    반환: \n
    result -- {full_text: 기사 본문, url: 기사 URL, ord: 순번} \n
    """

    return {"full_text": full_text, "url": url, "ord": ord}


SITE_NAVER_IT_GENERAL = "naver-it-general"
"""
네이버 IT 일반 사이트를 의미하는 문자열. \n
Article 테이블 내 site 칼럼에서 사용
"""