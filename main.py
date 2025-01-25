import os
import importlib
from telegram.ext import Application
from utils.misc import add_handlers
from dotenv import load_dotenv
load_dotenv()

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    kall = Application.builder().token(TOKEN).build()
    add_handlers(kall)
    kall.run_polling()

if __name__ == "__main__":
    main()
