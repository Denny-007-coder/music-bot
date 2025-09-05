
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Hello! I'm your music bot!")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔊 Playing music...")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    
    print("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
