from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "Type a keyword to see what happens!"
    )

def register(kall):
    kall.add_handler(CommandHandler("help", help))
