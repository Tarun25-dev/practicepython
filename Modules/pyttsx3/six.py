# user input voice
import pyttsx3
engine = pyttsx3.init()
choice = input("Enter 0 for male voice and 1 for Female voice: ")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[int(choice)].id)
engine.say("You choosen the right voice!")
engine.runAndWait()