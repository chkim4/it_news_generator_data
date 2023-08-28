"""
개별 동영상을 하나로 합쳐서 오늘 뉴스 동영상 생성
"""

from moviepy import editor
import os

from common._global import get_video_full_path
from common._generation import ONE_TTSS_PATH, ONE_IMGS_PATH, ONE_VIDEOS_PATH

def generate_final_video() -> None:
    """
    ONE_VIDEOS_PATH 폴더 내 모든 영상을 이어 최종 영상 생성 \n
    저장 경로: _global.get_video_full_path()의 반환 값
    """

    entries = os.scandir(ONE_VIDEOS_PATH)

    videos = []

    for entry in entries:
        if entry.is_file():
            video = editor.VideoFileClip(entry.path)
            videos.append(video)
            video.reader.close()
    
    final_video = editor.concatenate_videoclips(videos)
    final_video.write_videofile(get_video_full_path())

def delete_tmp_files():
    """
    최종 영상 생성 후 필요 없는 TTS, 이미지, 영상 파일 삭제 \n
    """

    dirs = [ONE_TTSS_PATH, ONE_IMGS_PATH, ONE_VIDEOS_PATH]

    for dir in dirs:
        entries = os.scandir(dir)
        
        for entry in entries:
            if entry.is_file():
                os.remove(entry.path)
