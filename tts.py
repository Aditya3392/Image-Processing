from gtts import gTTS
import os

def speak(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("/content/tts_output.mp3")
    os.system("mpg321 /content/tts_output.mp3")
