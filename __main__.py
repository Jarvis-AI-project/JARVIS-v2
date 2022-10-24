import functions.WakeWord as WakeWord
import functions.SpeechToText.azure as STT
import winsound
import features.DateTime.time as time

# verification
import functions.FaceRecognition as FaceID
if FaceID.FaceID() == True:
    print("FaceID: Verified")
elif FaceID.FaceID() == False:
    print("FaceID: Not Verified")
    exit()


while True:
    wake = WakeWord.wake_word_detection(
        model=['functions\WakeWord\jarvis_windows.ppn', 'functions\WakeWord\hey-jarvis_windows.ppn', 'functions\WakeWord\hi-jarvis_en_windows.ppn'])
    try:
        if wake == True:
            winsound.Beep(2500, 100)
            output_dict = STT.speech_to_text()
            print(output_dict)
            if output_dict['transcription'] != '':
                print('Analysing...')
                # --------features here------

        elif wake == False:
            WakeWord.reset()

        elif wake == 'KeyboardInterrupt':
            break

    except Exception as e:
        print('Unknown Error')
        print(e)
