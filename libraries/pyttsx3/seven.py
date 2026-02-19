# sound exact letters while typing 
import pyttsx3

while True:
    text = input("Type: ")
    if text == "done":
        break
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop() # resets the engine
    
# try in jupiter notebook if sound not working