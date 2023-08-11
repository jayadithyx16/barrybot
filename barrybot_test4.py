from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6407514901:AAFQepU0xaANs3fSqpSVtRosNsJ-rmbWp1k'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! Send me a file, document, video, photo, or text.")

def process_user_input(update: Update, context: CallbackContext) -> None:
    user_input = update.message.caption or update.message.text

    if user_input:
        # Task 1: Remove words starting with '[' or '@' and ending with ']' or ' '
        cleaned_input = ' '.join(word for word in user_input.split() if not (word.startswith('[') or word.startswith('@')))
        
        # Task 2: Remove '[' or '@' from the caption
        cleaned_input = cleaned_input.replace('[', '').replace('@', '')
        
        # Task 3: Remove unnecessary white spaces
        cleaned_input = ' '.join(cleaned_input.split())

        update.message.reply_text(f"Cleaned Caption: {cleaned_input}")
    else:
        update.message.reply_text("No caption or text found.")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document, process_user_input))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
