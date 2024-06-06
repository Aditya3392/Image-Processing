import pyttsx3

def speak(text, rate=1.4, voice_type="female", volume=1):
    try:
        engine = pyttsx3.init()
    except Exception as e:
        print(f"Error initializing pyttsx3: {e}")
        return

    # speech rate
    engine.setProperty('rate', rate * engine.getProperty('rate'))

    # Voice
    voices = engine.getProperty('voices')
    if voice_type == "female":
        engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    else:
        engine.setProperty('voice', voices[0].id)

    # Volume
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()
