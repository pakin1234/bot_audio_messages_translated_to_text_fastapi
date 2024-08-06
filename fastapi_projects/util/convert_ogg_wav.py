import soundfile as sf   #   pip install pysoundfile

def converting_from_ogg_to_wav(input_file: str, output_file: str):
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate)




# from pydub import AudioSegment

# def ogg_to_wav(input_file, output_file):
#     audio = AudioSegment.from_ogg(input_file)
#     audio.export(output_file, format="wav")

# input_file = "maybe-next-time.ogg"
# output_file = "maybe-next-time.wav"

# ogg_to_wav(input_file=input_file, output_file=output_file)
