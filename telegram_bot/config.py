from environs import Env

def load_bot_token_from_env():
    env = Env()
    env.read_env()

    return env.str("BOT_TOKEN")