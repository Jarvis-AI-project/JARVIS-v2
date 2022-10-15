import speech_recognition as sr
import winsound
import multiprocessing as mp

def speech_to_text():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Engine Listening...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        if r.recognize_google(audio, show_all=True) is not None:
            return {'text': r.recognize_google(audio), 
                    'confidence': r.recognize_google(audio, show_all=True)['alternative'][0]['confidence']}
        else:
            return {'text': r.recognize_google(audio), 'confidence': 0.0}

    except sr.UnknownValueError:
        return {'type': 'Error', 'data': 'Understanding Audio Error'}

    except sr.RequestError as e:
        print("\nCould not request results from Speech Recognition service; {0}".format(e))
        return {'type': 'Error', 'data': 'Connection Error'}
    
if __name__ == "__main__":
    while True:
        speech_to_text()