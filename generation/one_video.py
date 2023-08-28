"""
TTS + 이미지 => 동영상 생성 \n

TTS와 이미지는 특정 순번으로 각 하나씩만 선택 \n

ex. 순번(ord) = 1 -> tts_1.mp3와 img_1.jpg의 조합으로 동영상 생성
"""

from moviepy import editor
import os 

from common._generation import ONE_TTS_PATH, ONE_IMG_PATH, ONE_VIDEO_PATH
from common._generation import IMG_EXTENDER, TTS_EXTENDER, VIDEO_EXTENDER
from generation.one_img import generate_one_img
from generation.one_tts import generate_one_tts

def generate_one_video(content: str, ord: int) -> None:
    """
    영상 생성 후 common._generation.ONE_VIDEO_PATH에 저장 \n
    
    매개변수: \n
    content -- 읽을 글자 (str) \n
    ord -- 순번 (int) \n
    """

    str_ord = str(ord) 

    generate_one_tts(content, ord)
    generate_one_img(content, ord)


    audio_path = os.path.join(ONE_TTS_PATH + str_ord + TTS_EXTENDER)
    img_path_str = ONE_IMG_PATH + str_ord  + IMG_EXTENDER
    video_path = os.path.join(ONE_VIDEO_PATH + str_ord + VIDEO_EXTENDER)

    # gTTS로 만든 mp3파일 읽어오기
    audio = editor.AudioFileClip(audio_path)

    # 영상 길이
    duration = audio.duration
    
    # 소리가 없는 영상 제작 (jpg -> mp4)
    no_audio_video = editor.ImageClip(img_path_str, duration=duration)
    
    # 영상 내 소리 설정 및 파일 저장
    video = no_audio_video.set_audio(audio)
    video.fps = 24
    video.write_videofile(video_path)

    print("video is generated")