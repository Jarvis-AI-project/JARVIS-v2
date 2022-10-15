import WakeWord
import SpeechToText
WakeWord.wake_word_detection(
    model=['WakeWord\jarvis_windows.ppn', 'WakeWord\hey-jarvis_windows.ppn', 'WakeWord\hi-jarvis_en_windows.ppn'])
output = SpeechToText.speech_to_text()
print(output)