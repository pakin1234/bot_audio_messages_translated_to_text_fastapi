from fastapi import APIRouter, UploadFile, File
import speech_recognition as sr
import ffmpeg
import shutil
import os

from util.main_audio import all_converting



router = APIRouter()

@router.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):

    # !!!!!!!!!!!!!!!!!!!!!make more optimized file paths!!!!!!!!!!!!!!!!
    input_file_path = f"C:\\Users\\HP\\audio_fastapi\\tester_audio_input_files\\{file.filename}"
    output_file_path = "C:\\Users\\HP\\audio_fastapi\\tester_audio_input_files\\" + "".join(file.filename.split(".")[0]) + ".wav"

    converted_text = all_converting(input_file_path, output_file_path, file)
    
    os.remove(input_file_path)
    os.remove(output_file_path)

    return converted_text


@router.get("/test-endpoint")
async def test_function():
    return {"data": "test-completed:))"}