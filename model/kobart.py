"""
kobart 모델 뉴스 요약

사용 모델: https://huggingface.co/ainize/kobart-news
"""

from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

#  Load Model and Tokenize
tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/kobart-news")
model = BartForConditionalGeneration.from_pretrained("ainize/kobart-news")


def kobart_summary(content: str) -> str: 
    """
    kobart-news 모델로 문서 요약 \n
   
    매개변수: \n
    content -- 요약에 사용할 원문 기사 (str) \n

    \n
    
    반환: \n
    result -- content를 생성 요약 1문장으로 요약한 결과 (str) \n
    """

    input_ids = tokenizer.encode(content, return_tensors="pt", max_length = 1024, truncation=True)

    summary_text_ids = model.generate(
        input_ids=input_ids,
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        length_penalty=2.0,
        max_length=142,
        min_length=56,
        num_beams=4,
    )

    return tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)