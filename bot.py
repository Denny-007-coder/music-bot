import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text("🎵 Hello! I'm your music bot!")

async def play(update: Update, context):
    await update.message.reply_text("Playing music...")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.run_polling()
