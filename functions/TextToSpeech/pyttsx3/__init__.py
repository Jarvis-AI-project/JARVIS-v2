import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed=170
engine.setProperty('rate', voicespeed)
engine.say("hello, sir i am your voice assistant")
engine.say("how can i help you")
engine.runAndWait()