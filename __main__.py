import functions.WakeWord as WakeWord
import functions.SpeechToText.azure as STT
import winsound
import features.DateTime.time as time
import re
import features.music.spotify as spotify
import features.music.spotify.azure_sdk as azure_sdk

# verification
import functions.FaceRecognition as FaceID
if FaceID.FaceID() == True:
    print("FaceID: Verified")
elif FaceID.FaceID() == False:
    print("FaceID: Not Verified")
    us = input('Do you want to verify by password? (y/n): ')
    if us.lower() == 'y':
        passw = input('Password: ')
        if passw == '1234':
            print('Password: Verified')
        else:
            print('Password: Not Verified')
            exit()
    else:
        print('Password: Not Verified')
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
                user_intent = azure_sdk.azure_query(command, "JARVIS-MAIN", 'v0.1-dep1')
                # --------<features here>--------
                if user_intent['intent'] == 'Jarvis.MusicControls':
                    spotify.spotify_sdk(command)
                
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