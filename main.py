import WakeWord
import SpeechToText.azure as STT
import winsound
import functions.DateTime.time as time

while True:
    wake = WakeWord.wake_word_detection(
        model=['WakeWord\jarvis_windows.ppn', 'WakeWord\hey-jarvis_windows.ppn', 'WakeWord\hi-jarvis_en_windows.ppn'])
    try:
        if wake == True:
            winsound.Beep(2500, 100)
            output_dict = STT.speech_to_text()
            print(output_dict)
            if output_dict['transcription'] != '':
                print('Analysing...')
                if 'time' in output_dict['transcription']:
                    print(time.time_now())
        elif wake == False:
            WakeWord.reset()
        
        elif wake == 'KeyboardInterrupt':
            break

    except Exception as e:
        print('Unknown Error')
        print(e)