"""
루트 폴더에서 주로 사용할 것으로 예상하는 공통 함수, 전역 변수 등
"""
from datetime import datetime, timedelta, timezone
from common._generation import VIDEO_EXTENDER


SITE_NAVER_IT_GENERAL = "naver-it-general"
"""
네이버 IT 일반 사이트를 의미하는 문자열. \n
Article 테이블 내 site 칼럼에서 사용
"""

VIDEO_LOCATION_PREFIX = "/video/"
"""
Video 테이블의 location 칼럼에 저장할 경로의 앞부분 \n
ex. '/video/170113.mp4' => /video/ 에 해당
"""

def get_video_full_path() -> str:
    """
    최종 생성된 영상의 저장 경로 (파일명 포함) \n
    파일명에 날짜 정보를 기재해야 하므로 전역 변수가 아닌 함수로 정의함 \n
    cf. URL, glob 등을 고려하여 파일에 특수문자를 삽입하지 않음

    반환: \n
    video_path -- 동영상을 저장할 경로 

    """
    
    prefix = "video/"

    timezone_kst = timezone(timedelta(hours=9))
    t = datetime.now(timezone_kst).strftime("%Y%m%d")

    video_full_path = prefix + t + VIDEO_EXTENDER

    return video_full_path
