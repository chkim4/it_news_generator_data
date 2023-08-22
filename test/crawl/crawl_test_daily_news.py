"""
하루 뉴스 크롤링 \n
사이트: Naver news \n
카테고리: IT 일반
"""

from bs4 import BeautifulSoup
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230')

soup=BeautifulSoup(browser.page_source, "html.parser")

ul = soup.find('ul', 'type06_headline')
a = ul.findChildren('a')
i = 1

for child in a:
    print(str(i) + "th child")
    browser.get(child['href'])
    child_soup = BeautifulSoup(browser.page_source, "html.parser")
    div = child_soup.find_all('div',{'id': 'dic_area'})
    i+=1
    
    for div_child in div:
        print(div_child.get_text())
        print('--------------------')

