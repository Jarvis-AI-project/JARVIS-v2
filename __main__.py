import functions.WakeWord as WakeWord
import functions.SpeechToText.azure as STT
import winsound
import features.DateTime.time as time
import re
import features.music.spotify as spotify

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
            command = (output_dict['transcription']).lower()
            if command != '':
                print('Analysing...')
                # --------<features here>--------
                if 'spotify' in command:
                    spotify.spotify_sdk(command)
                    print('Spotify SDK: Done')

                #elif

                else:
                    print('Command not found')

                # --------</features here>--------

        elif wake == False:
            WakeWord.reset()

        elif wake == 'KeyboardInterrupt':
            break

    except Exception as e:
        print('Unknown Error')
        print(e)