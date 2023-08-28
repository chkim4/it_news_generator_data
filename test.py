# 테스트용. 끝날 시 삭제
from generation.one_img import generate_one_img
from generation.one_tts import generate_one_tts
from generation.one_video import generate_one_video

def gen_test(content, ord):
    generate_one_img(content, ord)
    generate_one_tts(content, ord)
    generate_one_video(ord)