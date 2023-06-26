"""
TTS + 이미지 -> 영상 (mp4)

참고: https://medium.com/@kamaljp/text-to-video-pipeline-python-automation-using-open-ai-models-f4341555c8d9
"""

# pip install mutagen
# pip install Pillow
from mutagen.mp3 import MP3 
from PIL import Image 
from pathlib import Path
from moviepy import editor
import os 

#Pre requisites
get_path ='C:/develop/toy/it_news_generator/test'
audio_path = "myFirstMP3.mp3"
video_path = "myFirstVideo.mp4"
folder_path = 'C:/develop/toy/it_news_generator/test'
full_audio_path = os.path.join(get_path,audio_path)
full_video_path = os.path.join(get_path,video_path)

# Reading in the mp3 that we got from gTTS

song = MP3(full_audio_path)
audio_length = round(song.info.length)
audio_length

# Globbing the images and Stitching it to for the gif

path_images = Path(folder_path)

images = list(path_images.glob('*.jpg'))

image_list = list()

for image_name in images:
    image = Image.open(image_name).resize((800, 800), Image.ANTIALIAS)
    image_list.append(image)
    
#Checking Audio length

length_audio = audio_length
duration = int(length_audio / len(image_list)) * 1000
print(duration)

#Creating Gif

image_list[0].save(os.path.join(folder_path,"temp.gif"),
                   save_all=True,
                   append_images=image_list[1:],
                   duration=duration)

# Creating the video using the gif and the audio file

video = editor.VideoFileClip(os.path.join(folder_path,"temp.gif"))
print('done video')

audio = editor.AudioFileClip(full_audio_path)
print('done audio')

final_video = video.set_audio(audio)
print('Set Audio and writing')

final_video.set_fps(60)

final_video.write_videofile(full_video_path)

# The final mp4 file in the folder