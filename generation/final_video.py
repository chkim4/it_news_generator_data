"""
개별 동영상을 하나로 합쳐서 오늘 뉴스 동영상 생성
"""

from moviepy import editor
import os
import pathlib

from common._global import get_video_full_path
from common._generation import ONE_TTSS_PATH, ONE_IMGS_PATH, ONE_VIDEOS_PATH

def generate_final_video() -> str:
    """
    ONE_VIDEOS_PATH 폴더 내 모든 영상을 이어 최종 영상 생성 \n
    저장 경로: _global.get_video_full_path()의 반환 값 \n 

    반환: \n
    video_path -- 생성된 영상이 저장된 상대 경로 (get_video_full_path()) (str)
    """

    entries = os.scandir(ONE_VIDEOS_PATH)

    videos = []

    for entry in entries:
        if entry.is_file():
            video = editor.VideoFileClip(entry.path)
            videos.append(video)
            video.reader.close()
    
    final_video = editor.concatenate_videoclips(videos)
    
    video_path = get_video_full_path()

    # 최종 영상 경로에 있던 이전 영상 제거
    entries = os.scandir(pathlib.Path(video_path).parent)
    for entry in entries:
        os.remove(entry)

    # 생성한 영상 저장
    final_video.write_videofile(video_path)
    return video_path


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