"""
검증용 데이터 중 100건 추출 \n
데이터셋 출처: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=97 \n
(뉴스 기사 데이터만 사용)
"""
import json
from pathlib import Path

original_data = {}
edited_data = {'documents': []}

base_path = Path(__file__).parent
file_path = (base_path / './dataset/document_summary/news_valid_original.json').resolve()

# 원래 데이터셋 불러오기
with open(file_path, 'r', encoding='UTF-8') as f:
    original_data = json.load(f)

full_text_list = []
extractive_list = []
abstractive_list = []

# n: 추출할 데이터 수 / file_name: 저장할 파일명
n = 100
file_name = 'edited_valid_100.json'

# 저장 형태
# edited_data = {
#    documents: [
#       {   (기사1)
#           text: (신문 기사, str),
#           extractive: (추출 요약, str),
#           abstractive: (생성 요약, str)
#        }, 
#        {   (기사2)
#           text: (신문 기사, str),
#           extractive: (추출 요약, str),
#           abstractive: (생성 요약, str)
#        }
#   ]
# }

# range 안의 값을 통해 생성할 데이터 수 결정
for i in range(n):
    _json = {'text': '', 'extractive': '', 'abstractive': ''}
    text_list = []
    
    for t in original_data['documents'][i]['text']:
        text_list.append(t[0]['sentence'])     
    
    _json['text'] = ''.join(text_list)

    extractive_list = original_data['documents'][i]['extractive']
    extractive_list.sort() # 원본 데이터의 extractive 필드 내 정렬이 안 되어 있는 경우가 있음 
    count = 0
    text_list = []

    # 문서 요약 데이터 구조:
    # text: [{index: 1, sentence: '한 문장'}] 
    #       혹은 [{index: 1, sentence: '한 문장'}, {index: 2, sentence: '한 문장'}]
    # 또한 extractive 필드의 값은 index의 값으로 이루어져 있으므로, 해당 문장을 찾기 위해서는 'text'를 전부 순회해야 함 
    # extractive의 원소 개수는 무조건 3이므로 break 조건으로 추출 요약문을 3개 추가했을 때로 설정함

    for paragraph in original_data['documents'][i]['text']:
        for sentence in paragraph:
            if sentence['index'] == extractive_list[0]:
                text_list.append(sentence['sentence'])
                extractive_list.pop(0)
                count+=1
                if count == 3:
                    break
        
        if count == 3:
            break

    _json['extractive'] = ''.join(text_list)
    _json['abstractive'] = original_data['documents'][i]['abstractive'][0]

    edited_data['documents'].append(_json)

# 생성한 json 파일을 컴퓨터에 저장

file_path = '../dataset/document_summary/' + file_name
full_file_path = (base_path / file_path).resolve()

with open(full_file_path, "w") as json_file:
    json.dump(edited_data, json_file, ensure_ascii=False)