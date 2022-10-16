import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

def synthesize_to_speaker():
    speech_config = speechsdk.SpeechConfig(
        subscription="a9046a1de2d54623ba05be25b9c2db19", region="centralindia")
    speech_config.speech_synthesis_voice_name = 'en-US-AmberNeural'
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async("hello world")

synthesize_to_speaker()