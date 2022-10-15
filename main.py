import WakeWord
import SpeechToText.azure as STT
import winsound
while True:
    wake = WakeWord.wake_word_detection(
        model=['WakeWord\jarvis_windows.ppn', 'WakeWord\hey-jarvis_windows.ppn', 'WakeWord\hi-jarvis_en_windows.ppn'])
    try:
        if wake == True:
            winsound.Beep(2500, 100)
            output = STT.speech_to_text()
            print(output)
        elif wake == False:
            WakeWord.reset()
        
        elif wake == 'KeyboardInterrupt':
            break

    except Exception as e:
        print('Unknown Error')
        print(e)