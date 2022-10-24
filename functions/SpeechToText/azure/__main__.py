import __init__ as SpeechToTextAzure
import winsound
while True:
    winsound.Beep(2500, 100)
    print(SpeechToTextAzure.speech_to_text())