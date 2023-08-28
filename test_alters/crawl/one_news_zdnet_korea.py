"""
뉴스 기사 1개 크롤링 \n
사이트: zdnet 코리아 \n
카테고리: 최신 뉴스 \n
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import re

browser=webdriver.Chrome()
browser.get('https://zdnet.co.kr/view/?no=20230822164102')

soup=BeautifulSoup(browser.page_source, "html.parser")
article = soup.find('div', id= re.compile('^content-'))

ps = article.find_all('p')

for p in ps:
    plist = p.strings

    for p in plist:
        print(p)


