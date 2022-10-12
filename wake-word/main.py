import pvporcupine


porcupine = pvporcupine.create(
  access_key='MMvgSaJ5k6iELWtuyxz6R0nnz7exBVT56piX6Qq9cQViCVEK2OsbNQ==',
  keywords=['JARVIS']
)

def get_next_audio_frame():
  pass

while True:
  audio_frame = get_next_audio_frame()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index == 0:
      # detected `porcupine`
  elif keyword_index == 1:
      # detected `bumblebee`