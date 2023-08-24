"""
뉴스 영상 생성 및 기사 크롤링 실행
"""
from crawl.one_news_naver import crawl_one_news_naver
from model.kobart import kobart_summary


def generate_daily_news_naver():
    """
    오늘 네이버 IT 일반 뉴스 전체 페이지 크롤링 -> 기사 요약 -> DB 저장 \n

    아이디어 \n
    1. DB에 삽입할 데이터를 가공하기 위한 [{}] 형태의 데이터 생성 (articles_dict) \n  
    2. 크롤링하면서 각 dict에 데이터 추가 {full_text: 기사 본문, source: 기사 URL, order: 순번} \n
    3. 각 dict 내 'full_text'를 요약하여 'summary' 속성 추가 \n
    4. site, date 속성 일괄 추가 \n
    4. DB 저장을 위해 dict -> tuple로 변경 후 저장

    """

    # {full_text, source, order} 생성   
    # article_dict_list = crawl_daily_news_naver()

    # for article in article_dict_list:
    #     article['summary'] = kobart_summary(article['full_text']) 
    #     print("----------------------------")
    #     print("source: " , article['source'])
    #     print("order: " , article['order'])
    #     print("summary: " , article['summary'])

    print(kobart_summary(crawl_one_news_naver("https://n.news.naver.com/mnews/article/092/0002302952?sid=105")))

    
generate_daily_news_naver()






