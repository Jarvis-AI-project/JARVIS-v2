# pip install pipreqs
#pipreqs /path/to/project

import struct
import pyaudio
import pvporcupine

porcupine = None
paud = None
audio_stream = None

access_keys = [
    'otyT/UGS6tKCiLj0cktSjxshuMSNt6+fYVmuwfscF1cZYiysbWdRVA==',
    'MMvgSaJ5k6iELWtuyxz6R0nnz7exBVT56piX6Qq9cQViCVEK2OsbNQ==',
    'pXwEvAXJABqQf8hMoHFFGcsgkabxMPQMttKsdeyXRxEAL6r0VTbf9w==']


def wake_word_detection(model):

    try:
        for key in access_keys:
            try:
                porcupine = pvporcupine.create(
                    access_key=key,
                    keyword_paths=model)
                break
            except Exception as e:
                print('Could not connect by key: ' + key)
                print(e)

        print('hotword detection started')
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,
                                 channels=1,
                                 format=pyaudio.paInt16,
                                 input=True,
                                 frames_per_buffer=porcupine.frame_length)
        while True:
            try:
                keyword = audio_stream.read(porcupine.frame_length)
                keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)
                keyword_index = porcupine.process(keyword)
                if keyword_index >= 0:
                    print("hotword detected", keyword_index)
                    return True

            except KeyboardInterrupt:
                print('You pressed ctrl+C')
                return 'KeyboardInterrupt'
    except Exception as e:
        print('ERROR in hotword detection')
        print(e)
        return False

def reset():
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()

if __name__ == '__main__':

    wake_word_detection(
        model=['jarvis_windows.ppn', 'hey-jarvis_windows.ppn', 'hi-jarvis_en_windows.ppn'])