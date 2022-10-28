import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(string):
	engine=pyttsx3.init()
	engine.say(string)
	engine.runAndWait()

def userInput():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("SPEAK NOW")
		audio=r.listen(source)
		query=r.recognize_google(audio)
	return query

def out():
	query=userInput().lower()
	print(f"MANTHAN SAID:{query}")
	results=wikipedia.summary(query,sentences=3)
	print(results)
	speak("WIKIPEDIA SAID:")
	speak(results)

speak("HELLO SIR,HOW MAY I HELP YOU?")
speak("WHAT DO YOU WANT TO SEARCH ON WIKIPEDIA?")
out()

