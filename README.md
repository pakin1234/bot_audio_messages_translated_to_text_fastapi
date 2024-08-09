# Converting audio messages to text

AMT - web app with telegram bot, that can help you to convert audio messages to text

## Installation

Create virtual environment and activate it. Then install all libraries by typing in your terminal 

`pip install -r requirements.txt` 


## Usage

Before starting to work with bot you need to start uvicorn server:

`uvicorn fastapi_projects/main_fastapi:app --reload` 

### In telegram

Firstly, you need to start bot by running `bot.py` file in `telegram_bot` folder. Then just send bot in telegram an audio message, and bot will convert it to text and send you result.


### In browser

You can also use web app by going to `http://127.0.0.1:8000/file/upload-file`, after starting uvicorn server. 
For more comfortable work you can go to `http://127.0.0.1:8000/docs` and make requests with __Swagger UI__.


