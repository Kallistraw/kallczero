from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

KEYWORDS = {
    "hello": "Hi there! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Let me know if there's anything else."
}

async def keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()

    for keyword, response in KEYWORDS.items():
        if keyword in message:
            await update.message.reply_text(response)
            return

    await update.message.reply_text("Sorry, I don't understand that.")

def register(kall):
    kall.add_handler(MessageHandler(filters.TEXT, keyword))
