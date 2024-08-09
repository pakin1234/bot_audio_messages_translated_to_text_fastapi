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






















# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
# import requests

# TELEGRAM_BOT_TOKEN = "7070417314:AAECXlqpPJo2spG8WlWZiuv0ZwPPZi3IPhM"
# FASTAPI_URL = "http://127.0.0.1:8000/fileupload-file"

# # Функция обработки аудиосообщений
# def handle_voice_message(update: Update, context: CallbackContext):
#     voice_message = update.message.voice
#     voice_file = context.bot.get_file(voice_message.file_id)
#     audio_file = requests.get(f'https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{voice_file.file_path}')

#     # Отправка аудиофайла на FastAPI для конвертации в текст
#     url = FASTAPI_URL
#     files = {'audio_file': audio_file.content}
#     response = requests.post(url, files=files)


#     if response.status_code == 200:
#         text_result = response.json()["text"]
#         context.bot.send_message(chat_id=update.effective_chat.id, text=text_result)
#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка при конвертации аудио в текст")

# # Функция обработки команды /start
# def start(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Отправь мне аудиосообщение, и я его сконвертирую в текст.")

# def main():
#     # Создание объекта Updater и передача токена Telegram бота
#     updater = Updater(TELEGRAM_BOT_TOKEN)

#     # Получение диспетчера для регистрации обработчиков
#     dispatcher = updater.dispatcher

#     # Регистрация обработчика для команды /start
#     dispatcher.add_handler(CommandHandler("start", start))

#     # Регистрация обработчика для аудиосообщений
#     dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice_message))

#     # Запуск бота
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
