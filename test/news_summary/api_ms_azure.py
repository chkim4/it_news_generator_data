"""
Azure 문서요약 테스트

230821 현재 예시 기사 (총 5문장)를 한 문장으로 인식하여 미사용 
"""
# import os
# from azure.ai.textanalytics import TextAnalyticsClient
# from azure.core.credentials import AzureKeyCredential
# from pathlib import Path
# import json
# from azure.ai.textanalytics import ExtractSummaryAction

# key = os.environ.get('LANGUAGE_KEY')
# endpoint = os.environ.get('LANGUAGE_ENDPOINT')

# # 요약할 문장 불러오기
# base_path = Path(__file__).parent
# file_path = (base_path / './dataset/document_summary/edited_valid_500.json').resolve()

# test_data = []

# with open(file_path, 'r', encoding='CP949') as f:
#     test_data = json.load(f)

# sentence = test_data['documents'][0]['text']

# # 인증 과정 
# def authenticate_client():
#     ta_credential = AzureKeyCredential(key)
#     text_analytics_client = TextAnalyticsClient(
#             endpoint=endpoint, 
#             credential=ta_credential,
#             language='ko')
#     return text_analytics_client

# client = authenticate_client()

# # 추출 요약
# def sample_extractive_summarization(client):
#     poller = client.begin_analyze_actions(
#         [sentence],
#         actions=[
#             ExtractSummaryAction(max_sentence_count=3)
#         ],
#     )

#     document_results = poller.result()
#     for result in document_results:
#         extract_summary_result = result[0]  # first document, first result
#         if extract_summary_result.is_error:
#             print("...Is an error with code '{}' and message '{}'".format(
#                 extract_summary_result.code, extract_summary_result.message
#             ))
#         else:
#             print("Summary extracted: \n{}".format(
#                 " ".join([sentence.text for sentence in extract_summary_result.sentences]))
#             )

#sample_extractive_summarization(client)