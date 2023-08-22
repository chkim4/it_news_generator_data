"""
TTS 테스트

참고: https://goodsgoods.tistory.com/328
"""

from gtts import gTTS

def speak(text):

     tts = gTTS(text=text, lang='ko', slow=False)

     filename='test/myFirstMP3.mp3'

     tts.save(filename)

speak("안녕! 세상아")