from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import requests

from config import load_bot_token_from_env

BOT_TOKEN = load_bot_token_from_env()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer("Hello, i can help you to convert audio messages to text:))")

async def process_help_command(message: Message):
    await message.answer("Send me an audio message and i will send your text message:))")


async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "saved_file.ogg")
    
    text = send_audio_to_convert(file_name="saved_file.ogg")

    await message.answer(text)

def send_audio_to_convert(file_name: str):
    URL = "http://127.0.0.1:8000/file/upload-file"
    files = {
        "file": open("saved_file.ogg", "rb")
    }
    response = requests.post(URL, files=files)
    print("Converted text: \n", response.text)
    return response.text


dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_start_command, Command(commands="help"))
dp.message.register(voice_message_handler, F.voice)


if __name__ == "__main__":
    dp.run_polling(bot)
