from gtts import gTTS
from common._generation import ONE_TTS_PATH, TTS_EXTENDER

def generate_one_tts(content: str, ord: int) -> None:
    """
    TTS 생성 후 common._generation.ONE_TTS_PATH에 저장 \n
    매개변수: \n
    content -- 읽을 글자 (str) \n
    ord -- 순번 (int) \n
    """

    tts = gTTS(text=content, lang='ko', slow=False)

    name = ONE_TTS_PATH + str(ord) + TTS_EXTENDER

    tts.save(name)

    print("TTS is generated")