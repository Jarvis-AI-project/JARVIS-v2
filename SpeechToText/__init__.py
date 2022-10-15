import speech_recognition as sr


def speech_to_text():
    try:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Engine Listening...")
            audio = r.listen(source, timeout=None, phrase_time_limit=None, snowboy_configuration=None)
            print('Processing...')
        # recognize speech using Google Speech Recognition

        output = r.recognize_google(audio, language='en-US', show_all=True)

        if output is not None:
            return {'text': output,
                    'confidence': output['alternative'][0]['confidence']}
        elif output is None:
            return {'transcription': output, 'confidence': 0.0}
        else:
            return {'type': 'Error', 'data': 'Unknown Error in Google Speech Recogition'}

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
