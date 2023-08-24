"""
뉴스 기사 1개 크롤링 \n
카테고리: IT 일반
"""

from bs4 import BeautifulSoup
from selenium import webdriver

def crawl_one_news_naver(url: str) -> str: 
    """
    네이버 뉴스 기사 1개 크롤링  \n
    매개변수: \n
    url -- 크롤링하고자 하는 뉴스의 URL (str) \n

    \n
    
    반환: \n
    result -- 기사 본문을 크롤링한 결과 (str) \n
    """

    browser=webdriver.Chrome()
    browser.get(url)
    soup=BeautifulSoup(browser.page_source, "html.parser")

    article = soup.find('article',{'id': 'dic_area'})

    full_text = " "

    for paragraph in article:
        full_text += paragraph.text

    return full_text
