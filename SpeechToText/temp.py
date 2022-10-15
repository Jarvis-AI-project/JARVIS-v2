import azure.cognitiveservices.speech as speechsdk


def recognize_from_mic():

    speech_config = speechsdk.SpeechConfig(subscription="95aa2e3713c5421683334dd5decb6fff", region="centralindia")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)


recognize_from_mic()