from fastapi import UploadFile

import shutil
import ffmpeg
import speech_recognition as sr

def save_convert_to_wav(input_file_path: str, output_file_path: str, file: UploadFile):
    with open(input_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    (
        ffmpeg.input(filename=input_file_path)
        .output(output_file_path)
        .overwrite_output()
        .run()
    )

def convert_audio_to_text(output_file_path: str):
    r = sr.Recognizer()

    audio_file = sr.AudioFile(output_file_path)

    with audio_file as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data, language="ru-RU")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def all_converting(input_file_path: str, output_file_path: str, file: UploadFile):
    save_convert_to_wav(input_file_path, output_file_path, file)
    text_result = convert_audio_to_text(output_file_path)

    return text_result
    


