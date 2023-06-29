"""
문서 요약 API 성능 비교
"""
import json
from pathlib import Path
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp

# 유사도 비교에 사용할 문장 불러오기 (contents)
base_path = Path(__file__).parent
file_path = (base_path / '../dataset/document_summary/edited_valid_500.json').resolve()

test_data = []

with open(file_path, 'r', encoding='CP949') as f:
    test_data = json.load(f)

contents = [test_data['documents'][0]['extractive']]

# API 비용 들어가니 네이버 Clova를 통해 미리 요약한 문장 사용
naver_clova_extractive_result = "대한민국 5G 홍보대사\'를 자처한 문재인 대통령은 \"넓고, 체증 없는 \'통신 고속도로\'가 5G\"라며 \"대한민국의 대전환이 이제 막 시작됐다\"고 기대감을 높였다.\n문 대통령은 8일 서울 올림픽공원에서 열린 5G플러스 전략발표에 참석해 \"5G 시대는 우리가 생각하고, 만들면 그것이 세계 표준이 되는 시대\" 라며 \"5G는 대한민국 혁신성장의 인프라\"라고 강조했다.\n문 대통령은 \"5G가 각 분야에 융합되면, 정보통신산업을 넘어 자동차, 드론(무인항공기), 로봇, 지능형 폐쇄회로TV(CCTV)를 비롯한 제조업과 벤처에 이르기까지 우리 산업 전체의 혁신을 통한 동반성장이 가능하다\"고 밝혔다.'"

# 유사도 검증 시작

# 벡터 사이의 거리를 구하는 함수
def dist_raw(v1, v2):
    delta = v1-v2
    
    return sp.linalg.norm(delta.toarray())

t = Okt()

# TF-IDF 시작
vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')

# 정답 문장 벡터화
contents_tokens = [t.morphs(contents[0])]

contents_for_vectorize = []

for content in contents_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
    
    contents_for_vectorize.append(sentence)

X = vectorizer.fit_transform(contents_for_vectorize)
num_samples, num_features = X.shape

# 네이버 클로바 문장 벡터화
new_post = [naver_clova_extractive_result]
new_post_tokens = [t.morphs(row) for row in new_post]

new_post_for_vectorize = []

for content in new_post_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
    
    new_post_for_vectorize.append(sentence)

new_post_vec = vectorizer.transform(new_post_for_vectorize)

post_vec = X.getrow(0)
d = dist_raw(post_vec, new_post_vec)

print("distance: " , d)
print('contents_for_vectorize: ', contents_for_vectorize)
print("new_post_for_vectorize: ", new_post_for_vectorize)