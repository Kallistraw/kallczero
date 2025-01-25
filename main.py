import os
import importlib
from telegram.ext import Application
from utils.misc import add_handlers
from dotenv import load_dotenv
from logging import basicConfig, INFO
load_dotenv()





_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S"
)


def main():
    TOKEN = os.getenv("BOT_TOKEN")
    kall = Application.builder().token(TOKEN).build()
    add_handlers(kall)
    print(add_handlers(kall))
    kall.run_polling()

if __name__ == "__main__":
    main()
