"""
하루 뉴스 기사 크롤링 \n
사이트: 네이버 뉴스 \n
카테고리: IT 일반
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import re

def crawl_daily_news_naver() -> list: 
    """
    오늘 네이버 IT 일반 뉴스 전체 페이지 크롤링

    \n
    
    반환: \n
    result -- 230823 현재 기준: [크롤링할 페이지의 최종값, 마지막 페이지, 마지막 순번]이지만, 교체 예정 \n
    """

    browser=webdriver.Chrome()
    default_url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&page='
    
    url = default_url + "1"
    soup=get_soup(url, browser)
    
    # page: 크롤링할 페이지
    # nums: 230823 현재 - 크롤링한 기사 개수 확인용으로 사용. 기사 순번으로 사용 가능할 것으로 예상
    # max_page: 1페이지 화면에서 가장 큰 페이지 번호
    # is_next_set_exists: '다음' 버튼 존재 여부
    page = 1
    nums = 0 
    max_page, is_next_set_exists = get_max_page(soup.find('div', 'paging'))
    
    while page <= max_page: 

        # 현재 페이지 크롤링 
        uls = soup.find_all('ul', {"class": re.compile('^type06')})
        
        for ul in uls:
            lis = ul.find_all('li')
            
            for li in lis: 
                a = li.select_one('dl > dt > a')
                browser.get(a['href'])
                child_soup = BeautifulSoup(browser.page_source, "html.parser")
                div = child_soup.find_all('article',{'id': 'dic_area'})
                nums+=1
                
        # 다음 페이지 호출
        page += 1

        # 다음 페이지 크롤링
        # 230824 현재 (요청 페이지 > 전체 페이지) 일 경우 가장 마지막 페이지로 연결
        #   - ex. 요청 페이지: ...&page=100, 전체 페이지: 11 => 11페이지로 연결
        #   - 그러므로 if 문 전에 아래 코드를 사용해도 무방함.  
        #      url = default_url + str(page)
        #      soup = get_soup(url, browser)
        # 하지만 추후 네이버 뉴스 페이지 수정을 고려하여 그렇게 처리하지 않음. 
        if page <= max_page: 
            url = default_url + str(page)
            soup = get_soup(url, browser)
            continue
        
        # (page > max_page) && (is_next_set_exists)
        # max_page 갱신
        elif is_next_set_exists:
            url = default_url + str(page)
            soup = get_soup(url, browser)
            max_page, is_next_set_exists = get_max_page(soup.find('div', 'paging'))
        
        # 크롤링 완료
        else:
            break

    return [page, max_page, nums]


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


result = crawl_daily_news_naver()
print(result)