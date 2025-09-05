import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Hello! I'm your music bot! Type /play")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔊 Playing music...")

def main():
    """Start the bot."""
    try:
        # Create the Application
        application = Application.builder().token(TOKEN).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("play", play))

        # Start polling
        logger.info("Bot started polling...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
