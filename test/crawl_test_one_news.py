"""
Crawl for one news 
site: Naver news, zdnet korea
"""

from bs4 import BeautifulSoup
from selenium import webdriver

# zdnet korea
# browser=webdriver.Chrome()
# browser.get('https://zdnet.co.kr/view/?no=20230615184539')

# soup=BeautifulSoup(browser.page_source, "html.parser")

# p = soup.find_all('p')

# for child in p:
#     print(child.contents)

# naver news
browser=webdriver.Chrome()
browser.get('https://n.news.naver.com/mnews/article/215/0001109625?sid=105')

soup=BeautifulSoup(browser.page_source, "html.parser")

div = soup.find_all('div', {'id': 'dic_area'})

for child in div:
    print('--------------------')
    print(child.get_text())
    print('--------------------')

