from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the bot! Type a keyword to get started."
    )

def register(kall):
    kall.add_handler(CommandHandler("start", start))
