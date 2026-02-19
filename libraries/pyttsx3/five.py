# dynamically switching voice during runtime
import pyttsx3 
engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print(voice.name)
# there are two voices only in voices such as 
# Microsoft David Desktop - English (United States)
# Microsoft Zira Desktop  -  English (United States)
engine.setProperty("voice",voices[0].id)
engine.say("Now i changed my voice")
engine.runAndWait()
