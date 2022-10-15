import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def speak():
    speech_config = speechsdk.SpeechConfig(
        subscription="26b8575c3dbc453cbb515a5d02d77338", region="centralindia")
    speech_config.speech_synthesis_voice_name = "en-US-JessaNeural"
    audio_config = AudioOutputConfig(
        use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async("hello world")


speak()
