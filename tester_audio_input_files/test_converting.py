import ffmpeg

output = (
    ffmpeg.input("audio_2024-07-27_12-35-17.ogg")
    .output("test1.wav")
    .overwrite_output()
    .run()
)



