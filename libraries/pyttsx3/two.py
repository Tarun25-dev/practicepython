# change voice 
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices") # get the current voice and change that using setProperty()
engine.setProperty("voice",voices[1].id) # 1 refers to female and 0 refers to male(also depends on system(os))
engine.say("Happy Birthday To You!..")
engine.runAndWait()
# why .id beacuse each voice has their unique id so we need to connect if you want to see that id then type print(voice.id)