import pyttsx3
engine = pyttsx3.init()
# initializes the speech engine
# it loads the text-to-speech driver, prepares the voice system, returns an engine object, allows you to control voice,speed,volume,etc.
# without init() you cant use .say() and .runAndWait().
engine.say("Hello, My name is Tharun, Welcome to Text-to-Speech in Python.")
engine.runAndWait() # default voice is Men