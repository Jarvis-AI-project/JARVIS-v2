import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
  
# for voice in voices:
#     # to get the info. about various voices in our PC 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)

# Changing index, changes voices. o
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.say("hello, sir i am your voice assistant")
engine.say("how can i help you")
engine.runAndWait()