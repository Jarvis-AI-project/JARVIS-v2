# pip install azure-cognitiveservices-speech
import azure.cognitiveservices.speech as speechsdk


def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription="95aa2e3713c5421683334dd5decb6fff", region="centralindia")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Listining...")
    result = speech_recognizer.recognize_once_async().get()

    return {'transcription': result.text,
            'type':result.reason,
            'confidence':'to be implimented'}


if __name__ == '__main__':
    out = speech_to_text()
    print(out)