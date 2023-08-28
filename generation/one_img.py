"""
기사 요약문이 적힌 이미지 생성 \n
"""

from PIL import Image, ImageDraw, ImageFont
from common._generation import ONE_IMG_PATH, IMG_EXTENDER

def generate_one_img(content: str, ord: int) -> None:
    """
    TTS 생성 후 common._generation.ONE_IMG_PATH에 저장 \n
    매개변수: \n
    content -- 화면에 띄울 글자 (str) \n
    ord -- 순번 (int) \n
    """
    
    # name of the file to save
    name = ONE_IMG_PATH + str(ord) + IMG_EXTENDER
    font = ImageFont.truetype("generation/fonts/koub_batang_light.ttf", 40)
    
    # create new image
    image = Image.new(mode = "RGB", size = (1920,1080), color='White')
    draw = ImageDraw.Draw(image)
    
    splited_content = split_content(content)

    draw.text((100,540), splited_content, font=font, fill='Black', anchor="lm")
    image.save(name)

    print("img is generated")


def split_content(content: str) -> str:
    """
    글씨가 화면 밖으로 벗어나지 않도록 content를 쪼개는 함수 \n
    한 줄에 공백 제외 30글자 이상 혹은 문장 단위로 띄어쓰기함. \n
   
    매개변수: \n
    content -- 요약에 사용할 원문 기사 (str) \n

    \n
    
    반환: \n
    result -- content를 화면 밖으로 벗어나지 않도록 가공한 결과 (str) \n
    """
    
    words = content.split(" ")
    result = ""

    line_breaker=30
    current_len=0
    
    for word in words:
        
        result += word + " "
        current_len += len(word)

        if "." in word:
            result += "\n\n"
            current_len=0

        elif current_len>=line_breaker:
            result += "\n"
            current_len=0

    return result