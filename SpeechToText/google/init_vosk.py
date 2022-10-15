#vosk models at : https://alphacephei.com/vosk/models
#https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
#https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip
#https://alphacephei.com/vosk/models/vosk-model-hi-0.22.zip

from vosk import Model, KaldiRecognizer
import pyaudio

#indian english model
model = Model(r"model\vosk-model-en-in-0.5")
recogniser = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recogniser.AcceptWaveform(data):
        print(recogniser.Result())