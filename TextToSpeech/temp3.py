from voicemaker import Voicemaker

vm = Voicemaker()
vm.set_token('9729c060-4d7d-11ed-be8d-312d29edc20b')
vm.generate_audio_to_file(out_path='test.mp3', text="I met a traveller from an antique land Who said: Two vast and trunkless legs of stone Stand in the desert.")