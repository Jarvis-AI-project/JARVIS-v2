import WakeWord
import SpeechToText
import winsound
while True:
    try:
        if WakeWord.wake_word_detection(model=['WakeWord\jarvis_windows.ppn', 'WakeWord\hey-jarvis_windows.ppn', 'WakeWord\hi-jarvis_en_windows.ppn']) == True:
            winsound.Beep(2500, 100)
            output = SpeechToText.speech_to_text()
            print(output)
        else:
            WakeWord.reset()

    except Exception as e:
        print('Error is:' + e)
        WakeWord.reset()