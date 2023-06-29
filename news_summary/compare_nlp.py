"""
형태소 분석기 성능 비교
"""
import json
from pathlib import Path
from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
import time

# 예시 요약문 불러오기
base_path = Path(__file__).parent
file_path = (base_path / '../dataset/document_summary/edited_valid_500.json').resolve()

test_data = []

with open(file_path, 'r', encoding='CP949') as f:
    test_data = json.load(f)

# 후보 문장
contents = test_data['documents'][0]['extractive']

# 형태소 분석기 성능 비교
# 속도와 정확성 면을 고려하여 okt로 결정 (공식문서에 따르면 1,000건 이상 부터는 okt가 더 나음)

# Okt 성능 측정
start_time = time.time()
okt = Okt()
contents_tokens_okt = okt.morphs(contents)
duration = time.time() - start_time
print("okt: " , contents_tokens_okt)
print("time: ", str(duration), " sec")
print("------------------------------")

# kkma 성능 측정
start_time = time.time()
kkma = Kkma()
contents_tokens_kkma = kkma.morphs(contents)
duration = time.time() - start_time
print("kkma: " , contents_tokens_kkma)
print("time: ", str(duration), " sec")
print("------------------------------")

# komoran 성능 측정
start_time = time.time()
komoran = Komoran()
contents_tokens_komoran = komoran.morphs(contents)
duration = time.time() - start_time
print("komoran: " , contents_tokens_komoran)
print("time: ", str(duration), " sec")
print("------------------------------") 

# hannanum 성능 측정
start_time = time.time()
hannanum = Hannanum()
contents_tokens_hannanum = hannanum.morphs(contents)
duration = time.time() - start_time
print("hannanum: " , contents_tokens_hannanum)
print("time: ", str(duration), " sec")
print("------------------------------")