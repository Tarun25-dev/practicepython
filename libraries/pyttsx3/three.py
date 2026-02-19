# change speed - speed rate we can change means which controls how fast words are spoken 
# usually default rate is 200, which is a normal speed if you want faster you can increase or if you want slowly then use lessthan 200 also.

import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",180)
engine.say("Hello World!")
engine.runAndWait()