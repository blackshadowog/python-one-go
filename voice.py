from gtts import gTTS
import playsound
import os

def speak(text):
    print("Prime:", text)

    filename = "prime_response.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    playsound.playsound(filename)

    try:
        os.remove(filename)
    except:
        pass
