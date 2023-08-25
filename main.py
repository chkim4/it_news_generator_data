"""
뉴스 영상 생성 및 기사 크롤링 실행
"""

from model.kobart import kobart_summary
import datetime
import os
import dotenv
import oracledb

# 직접 제작
from common._global import SITE_NAVER_IT_GENERAL
from crawl.some_daily_news_naver import crawl_some_daily_news_naver

dotenv.load_dotenv()
DB_ID = os.environ.get("DB_ID")
DB_PASS = os.environ.get("DB_PASS")
DB_DSL = os.environ.get("DB_DSL")

def generate_daily_news_naver():
    """
    오늘 네이버 IT 일반 뉴스 전체 페이지 크롤링 -> 기사 요약 -> DB 저장 \n
    """

    # {full_text, url, ord} 생성 (크롤링을 통해서만 얻을 수 있으므로 별도 실행)
    # 230824 현재 테스트를 위해 한 개의 기사를 대상으로 함. 수정 요망
    article_dict_list = crawl_some_daily_news_naver()
    articles = []

    # articles ( list(tuple) ) 생성
    for idx, article in enumerate(article_dict_list):
        summary = kobart_summary(article['full_text'])
        created_at = datetime.datetime.now()
        print("idx: ", idx+1)
        print("url: " , article["url"])

        articles.append((summary, article["url"], article["ord"], 
                        SITE_NAVER_IT_GENERAL, created_at)) 
    
    print("summary is done")

    # articles를 DB에 삽입
    oracledb.init_oracle_client()
    con = oracledb.connect(user= DB_ID, password= DB_PASS, dsn=DB_DSL)
    cursor = con.cursor()

    cursor.executemany("""INSERT INTO ARTICLE (article_id, summary, url, ord, site, created_at) 
                        VALUES (ARTICLE_SEQ.NEXTVAL, :1, :2, :3, :4, :5)""", articles)
    
    con.commit()
    con.close()

generate_daily_news_naver()






