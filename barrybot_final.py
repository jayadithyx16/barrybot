import re
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6407514901:AAHU4wk67IGgKQIUslHGiMotggWZmwKFf90'

def remove_words(text):
    # Define the patterns to match
    patterns = [
        r'@\S+?(?:\]|\s|$)',
        r'^@.*?-',
        r'https\S+',
        r'(?i)fast download link.*?:',
        r'(?i)join.*?:',
        r'➠',
        r'#',
        r'@\S+ -',
        r'^\s*\u2705\s*-\s*',
        r'^\s*\u270D\uFE0F?\s*',
        r'^\s*\U0001F4AF\s*Uploaded\s*By\s*.*'
    ]
    
    # Apply the patterns and replace matching words with an empty string
    for pattern in patterns:
        text = re.sub(pattern, '', text)
    
    # Replace consecutive newline characters with a single newline
    text = re.sub(r'\n+', '\n', text)
    
    text = text.lstrip('-')
    if '📥 Upload :' not in text and '📥 𝗨𝗽𝗹𝗼𝗮𝗱 :' not in text:
        text += ' @projectorparadise'
    text = text.replace('📥 𝗨𝗽𝗹𝗼𝗮𝗱 :', '📥 𝗨𝗽𝗹𝗼𝗮𝗱 : @projectorparadise')
    text = text.replace('📥 Upload :', '📥 Upload : @projectorparadise')
  
    return text.strip()
    

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your caption cleaner bot. Send me a message with a caption to get started.")

def process_media(update: Update, context: CallbackContext) -> None:
    if update.message.caption:
        caption = update.message.caption
        cleaned_caption = remove_words(caption)
        update.message.reply_text(cleaned_caption)

def main() -> None:
    # Initialize the Updater with your bot token
    updater = Updater(TOKEN)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Register the handler for text messages with captions
    dispatcher.add_handler(MessageHandler(Filters.caption, process_media))
    # Register the handler for photos with captions
    dispatcher.add_handler(MessageHandler(Filters.photo & Filters.caption, process_media))
    # Register the handler for videos with captions
    dispatcher.add_handler(MessageHandler(Filters.video & Filters.caption, process_media))
    # Register the handler for documents with captions
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("application/pdf") & Filters.caption, process_media))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  