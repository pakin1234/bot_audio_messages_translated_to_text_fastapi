from audio_translate import converting_to_text
from convert_ogg_wav import converting_from_ogg_to_wav

input_file = "maybe-next-time.ogg"
output_file = "maybe-next-time-converted.wav"

converting_from_ogg_to_wav(input_file=input_file, output_file=output_file)
print("Successfully converted")

converting_to_text(output_file)
print("Successfully transcribed")


