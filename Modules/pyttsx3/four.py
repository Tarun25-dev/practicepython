# change volume up or down 
# usually the volume rate between the 0.0 to 1.0 (min and max)
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("volume",1.0)
engine.say("Indians loves india")
engine.runAndWait()