from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7204491219:AAEimNEQiTYenLd9pbjpehjMCPir1ctdH6g"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Send me a TeraBox link to get started.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    if "terabox" in user_msg or "terabox.com" in user_msg:
        await update.message.reply_text("🔄 Processing your TeraBox link... (Feature coming soon)")
    else:
        await update.message.reply_text("❗ Please send a valid TeraBox link.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()
