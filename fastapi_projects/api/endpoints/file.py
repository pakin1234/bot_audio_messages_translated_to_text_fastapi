from fastapi import APIRouter, UploadFile, File
import speech_recognition as sr
import ffmpeg
import shutil
import os

from util.convert_ogg_wav import converting_from_ogg_to_wav
from util.audio_translate import converting_to_text



router = APIRouter()

@router.post("upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    # создаем два пути для сохранения файлов один для файла ogg второй уже для конвертированного в wav файл
    input_file_path = f"C:\\Users\\HP\\audio_fastapi\\tester_audio_input_files\\{file.filename}"
    output_file_path = "C:\\Users\\HP\\audio_fastapi\\tester_audio_input_files\\" + "".join(file.filename.split(".")[0]) + ".wav"
    
    # записываем и сохраняем файл ogg
    with open(input_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # конвертируем файл в wav
    (
        ffmpeg.input(filename=input_file_path)
        .output(output_file_path)
        .overwrite_output()
        .run()
    )
    
    # конвертируем аудио в текст
    r = sr.Recognizer()

    audio_file = sr.AudioFile(output_file_path)

    with audio_file as source:
        audio_data = r.record(source)

    try:
        # print("Google Recognition: " + r.recognize_google(audio_data))
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    # удаляем оба файла !!! Надо вынести в функции все что можно !!! Может тогда заработает
    os.remove(input_file_path)
    os.remove(output_file_path)

    return {}










    # # return {"filename": file.filename}
    # file_path = f"C:\\Users\\HP\\audio_fastapi\\tester_audio_input_files\\{file.filename}"
    # with open(file_path, "wb") as buffer:
    #     buffer.write(await file.read())
    # print("--------------Written to buffer---------------------------")

    # # converting_from_ogg_to_wav(input_file: str, output_file: str):
    # print("--------------Before converting to wav---------------------------")
    # wav_path_file = file_path.replace(file_path.split(".")[-1], "wav")
    # print("--------------renaming the file---------------------------")
    
    # # converting_from_ogg_to_wav(file_path, wav_path_file)
    # ouput = (
    #     ffmpeg.input(filename=file_path)
    #     .output(wav_path_file)
    #     .overwrite_output()
    #     .run()
    # )
    # print("--------------Converted to wav---------------------------")


    # # text = converting_to_text(wav_path_file)
    # r = sr.Recognizer()

    # audio_file = sr.AudioFile(wav_path_file)

    # with audio_file as source:
    #     audio_data = r.record(source)

    # try:
    #     # print("Google Recognition: " + r.recognize_google(audio_data))
    #     text = r.recognize_google(audio_data)
    #     return text
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
    # print("--------------Converted to text---------------------------")
    # # recognizer = sr.Recognizer()
    # # with sr.AudioFile(wav_path) as source:
    # #     audio_data = recognizer.record(source)
    # #     text = recognizer.recognize_google(audio_data)

    # return {"text": text}

