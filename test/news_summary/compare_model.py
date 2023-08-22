"""
kobart 모델과 API 비교 \n

kobart: https://huggingface.co/ainize/kobart-news \n
API: 네이버 클로바, ChatGPT, 카카오 koGPT
"""
#-*- coding: utf-8 -*-
from transformers import AutoTokenizer, AutoModel
import torch
from pathlib import Path
import json
from api_kakao_kogpt import kogpt_summary
from api_naver_clova import clova_summary
from api_openai_chatgpt import chatgpt_summary
from kobart import kobart_summary

# 테스트 데이터 가져오기
base_path = Path(__file__).parent
file_path = (base_path / './dataset/document_summary/edited_valid_100.json').resolve()

test_data = []

with open(file_path, 'r', encoding='CP949') as f:
    test_data = json.load(f)

# 유사도 비교 모델 가져오기
tokenizer = AutoTokenizer.from_pretrained("klue/roberta-large")
model = AutoModel.from_pretrained("klue/roberta-large")

# 유사도 구하기
def get_similarity(text1: str, text2: str) -> float:
    """
    text1과 text2의 문장 유사도 반환 \n

    매개변수: \n
    text1 -- 비교할 문장1 (String) \n
    text1 -- 비교할 문장2 (String) \n
    
    \n

    반환: \n
    result -- 두 문장의 유사도 (float)
    """
    # 두 문장을 각각 tokenize (문장 -> 단어 분리)
    encoded_input = tokenizer([text1,text2], padding=True, truncation=True, return_tensors='pt')

    # 문장 내 모든 단어 임베딩 (단어 -> 벡터)
    with torch.no_grad():
        model_output = model(**encoded_input)

    # 풀링 (Pooling. 문장 내 단어들의 임베딩 결과를 토대로 문장을 임베딩)
    # 평균 풀링 (mean pooling): 각 단어를 나타내는 출력 벡터들의 평균을 문장 전체의 벡터로 간주
    # model_output[0]: 모든 토큰의 임베딩 결과를 지님.
    token_embeddings = model_output[0] 
    input_mask_expanded = encoded_input['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()
    sentence_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    # text1과 text2의 문장 임베딩 결과(벡터)를 코사인 유사도로 비교  
    cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
    output = cos(sentence_embeddings[0], sentence_embeddings[1])

    return torch.IntTensor.item(output)

# 각 모델의 유사도 평균 점수 저장 
chatgpt = 0
clova = 0
kogpt = 0
kobart = 0
idx = 0

for element in test_data["documents"]:
    chatgpt += get_similarity(chatgpt_summary(element['text']), element['abstractive'])
    clova += get_similarity(clova_summary(element['text']), element['extractive'])
    kogpt += get_similarity(kogpt_summary(element['text']), element['abstractive'])
    kobart += get_similarity(kobart_summary(element['text']), element['abstractive'])
    idx +=1
    print( idx, " th element is done")

chatgpt /= 100
clova /= 100
kogpt /= 100
kobart /= 100

print("------result------")
print("chatgpt: ", chatgpt)
print("clova: ", clova)
print("kogpt: ", kogpt)
print("kobart: ", kobart)
