import WakeWord
import winsound
while True:
    try:
        if WakeWord.wake_word_detection(model=['WakeWord\jarvis_windows.ppn', 'WakeWord\hey-jarvis_windows.ppn', 'WakeWord\hi-jarvis_en_windows.ppn']) == True:
            winsound.Beep(2500, 100)
        else:
            WakeWord.reset()

    except:
        print('Unknown Error')