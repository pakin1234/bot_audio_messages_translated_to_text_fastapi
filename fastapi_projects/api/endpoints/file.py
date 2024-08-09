from fastapi import APIRouter, UploadFile, File

import os

from util.main_audio import all_converting



router = APIRouter()

@router.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):    
    input_file_path = f"..\\saved_audio_input_files\\{file.filename}"
    output_file_path = "..\\saved_audio_input_files\\" + "".join(file.filename.split(".")[0]) + ".wav"

    converted_text = all_converting(input_file_path, output_file_path, file)
    
    os.remove(input_file_path)
    os.remove(output_file_path)

    return converted_text