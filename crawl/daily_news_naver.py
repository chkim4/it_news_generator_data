"""
하루 뉴스 기사 크롤링 \n
사이트: 네이버 뉴스 \n
카테고리: IT 일반
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import re
from common._crawl import get_max_page
from common._crawl import get_soup
from common._crawl import convert_crawl_to_dict

def crawl_daily_news_naver() -> list: 
    """
    오늘 네이버 IT 일반 뉴스 전체 페이지 크롤링

    \n
    
    반환: \n
    result -- 'common._global.convert_crawl_to_dict'에서 정의한 자료 구조로 반환 
    """

    browser=webdriver.Chrome()
    default_url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&page='
    
    url = default_url + "1"
    soup=get_soup(url, browser)
    
    # page: 크롤링할 페이지
    # ord: 오늘 뉴스 내 각 기사의 순번
    # max_page: 1페이지 화면에서 가장 큰 페이지 번호
    # is_next_set_exists: '다음' 버튼 존재 여부
    page = 1
    ord = 1
    max_page, is_next_set_exists = get_max_page(soup.find('div', 'paging'))
    result = []
    
    while True:  

        # 현재 페이지 크롤링 
        uls = soup.find_all('ul', {"class": re.compile('^type06')})
        
        for ul in uls:
            lis = ul.find_all('li')
            
            for li in lis: 
                full_text = "" # 기사 내 본문 
                a = li.select_one('dl > dt > a')
                href = a['href']
                browser.get(href)
                child_soup = BeautifulSoup(browser.page_source, "html.parser")
                article = child_soup.find_all('article',{'id': 'dic_area'})
                
                for paragraph in article:
                    full_text += paragraph.text
                
                result.append(convert_crawl_to_dict(full_text, href, ord))
                ord+=1
                
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

    return result