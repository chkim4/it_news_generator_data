"""
generation 폴더에서 주로 사용할 것으로 예상하는 공통 함수, 전역 변수 등 \n
"""

ONE_DEFAULT_PATH = "generation/tmp/"
"""
한 개 기사에 대한 TTS, 이미지, 영상을 저장하는 공통 경로 \n
_generation.py 내에서 사용하기 위해 정의함
"""

ONE_TTS_PATH = ONE_DEFAULT_PATH + "tts/tts_"
"""
한 개 기사에 대한 TTS의 기본 경로 \n
"ONE_TTS_PATH + str(ord)" => 이런 식으로 사용하자
"""

ONE_IMG_PATH = ONE_DEFAULT_PATH + "img/img_"
"""
한 개 기사에 대한 이미지의 기본 경로 \n
"ONE_IMG_PATH + str(ord)" => 이런 식으로 사용하자
"""

ONE_VIDEO_PATH = ONE_DEFAULT_PATH + "video/video_"
"""
한 개 기사에 대한 영상의 기본 경로 (파일명 포함) \n
"ONE_VIDEO_PATH + str(ord)" => 이런 식으로 사용하자
"""

ONE_TTSS_PATH = ONE_DEFAULT_PATH + "tts/"
"""
낱개 TTS의 저장 경로 (파일명X) \n
TTS 삭제 시 사용
"""

ONE_IMGS_PATH = ONE_DEFAULT_PATH + "img/"
"""
낱개 이미지의 저장 경로 (파일명X) \n
이미지 삭제 시 사용
"""


ONE_VIDEOS_PATH = ONE_DEFAULT_PATH + "video/"
"""
낱개 영상의 저장 경로 (파일명X) \n
ONE_VIDEO_PATH에 있는 영상들을 연결할 때 사용
"""

TTS_EXTENDER = ".mp3"
"""
TTS 파일에 사용하는 확장자
"""

IMG_EXTENDER = ".jpg"
"""
이미지 파일에 사용하는 확장자
"""

VIDEO_EXTENDER = ".mp4"
"""
영상 파일에 사용하는 확장자
"""
