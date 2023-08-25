"""
crawl 폴더에서 주로 사용할 것으로 예상하는 공통 함수, 전역 변수 등 \n
230825 - 현재는 네이버 뉴스 크롤링 관련 함수만 존재
"""
from bs4 import BeautifulSoup

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

def get_max_page(pages) -> list:
    """
    현재 화면에서 가장 큰 페이지 값과 '다음' 버튼 유무 여부 반환 \n
    생각보다 반복적으로 쓰이는 코드라서 별도 함수 생성 \n
    
    매개변수: \n
    pages -- 네이버 뉴스 페이지 내 페이지 태그들 (soup.find('div', 'paging')) \n

    \n
    
    반환: \n
    list -- [max_page, is_next_set_exists] \n
         -- max_page: 현재 화면에서의 마지막 페이지 \n
         -- is_next_set_exists: 다음 페이지 목록 유무 여부 \n
            ex. 총 20 페이지, 현재 1페이지일 경우 True \n
    """

    max_page = 0
    is_next_set_exists = False
    
    # page_list 예시
    # 전체 11 페이지이고, 현재 1 페이지일 경우
    # ["1", "2", ... "10", "다음"]
    tmp_page_list = pages.text.split("\n") 
    page_list = list(filter(lambda element: element.strip(), tmp_page_list))

    # 다음 페이지 묶음이 있을 경우 (페이지 묶음: 10 페이지 단위. ex. 1 ~ 10, 11 ~ 20...)
    # ex. 총 11 페이지, 현재 페이지: 1 
    if page_list[-1] == '다음':
        max_page = int(page_list[-2]) + 1
        is_next_set_exists = True

    # 현재 페이지가 마지막 페이지 묶음에 속할 경우
    # ex. 총 19 페이지, 현재 페이지: 11
    else:
        max_page = int(page_list[-1])
    
    return [max_page, is_next_set_exists]


def get_soup(url: str, browser):
    """
    URL과 browser 기반으로 BeautifulSoup 객체 생성 \n
    생각보다 반복적으로 쓰이는 코드라서 별도 함수 생성 \n
    
    매개변수: \n
    url -- 크롤링하고자 하는 URL (String) \n
    browser -- selenium.webdriver \n

    \n
    
    반환: \n
    BeautifulSoup -- bs4.BeautifulSoup \n
    
    """

    browser.get(url)
    return BeautifulSoup(browser.page_source, "html.parser")
