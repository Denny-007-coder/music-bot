import os
from telegram.ext import Updater, CommandHandler
from telegram import Update
from telegram.ext import CallbackContext

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎵 Hello! I'm your music bot!")

def play(update: Update, context: CallbackContext):
    update.message.reply_text("Playing music...")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("play", play))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
