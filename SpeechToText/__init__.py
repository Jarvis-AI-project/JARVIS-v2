import speech_recognition as sr


def speech_to_text():
    try:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Engine Listening...")
            audio = r.listen(source, timeout=6)

        # recognize speech using Google Speech Recognition
        if r.recognize_google(audio, show_all=True) is not None:
            return {'text': r.recognize_google(audio),
                    'confidence': r.recognize_google(audio, show_all=True)['alternative'][0]['confidence']}
        else:
            return {'transcription': r.recognize_google(audio), 'confidence': 0.0}

    except sr.UnknownValueError as e:
        print(e)
        return {'type': 'Error', 'data': 'Understanding Audio Error'}

    except sr.RequestError as e:
        print(e)
        return {'type': 'Error', 'data': 'Connection Error'}

    except sr.WaitTimeoutError as e:
        print(e)
        return {'type': 'Error', 'data': 'Listning Timed Out While Waiting For Phrase to Start'}


if __name__ == "__main__":
    while True:
        speech_to_text()
