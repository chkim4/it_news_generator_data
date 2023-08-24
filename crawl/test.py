"""
뉴스 기사 1개 크롤링 \n
카테고리: IT 일반
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from common._global import convert_crawl_to_dict

def test(url: str) -> list: 
    """
    네이버 뉴스 기사 1개 크롤링  \n
    매개변수: \n
    url -- 크롤링하고자 하는 뉴스의 URL (str) \n

    \n
    
    반환: \n
    result -- 'common._global.convert_crawl_to_dict'에서 정의한 자료 구조로 반환\n
    """

    browser=webdriver.Chrome()
    browser.get(url)
    soup=BeautifulSoup(browser.page_source, "html.parser")

    article = soup.find('article',{'id': 'dic_area'})

    full_text = " "

    for paragraph in article:
        full_text += paragraph.text

    return [convert_crawl_to_dict(full_text, url, 1)]
