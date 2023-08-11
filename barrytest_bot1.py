from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InputMediaPhoto, InputMediaVideo, InputMediaDocument

Token: Final = '6407514901:AAFQepU0xaANs3fSqpSVtRosNsJ-rmbWp1k'
BOT_USERNAME: Final = '@barryallen16_bot'
async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hy man! what captions do you want me to add today')

async def help_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('I can add captions, remove whitespaces and more')

async def custom_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Automating.....')
def process_caption(caption: str) -> str:
    # Task 1: Remove words starting with '[' or '@' and end with ']' or ' '
    words = caption.split()
    filtered_words = [word for word in words if not (word.startswith('[') or word.startswith('@'))]
    processed_caption = ' '.join(filtered_words)
    
    # Task 2: Remove unnecessary white spaces
    processed_caption = ' '.join(processed_caption.split())

    return processed_caption
async def input_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter the text to add at the end of the caption:")
    context.user_data['waiting_for_input'] = True

# ... (inside handle_message())
if 'waiting_for_input' in context.user_data:
    user_input = text
    response = f"{response} {user_input}"
    context.user_data.pop('waiting_for_input')
else:
    await handle_message(update, context)  # Continue processing the message as before


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ... (your existing code)
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            processed_response = process_caption(new_text)  # Process the caption
            response = handle_response(processed_response)  # Handle the response
        else:
            return
    else:
        processed_response = process_caption(text)  # Process the caption
        response = handle_response(processed_response)  # Handle the response

    # Task 3: Add user input at the end of the caption
    user_input = input("Enter text to add at the end of the caption: ")
    response = f"{response} {user_input}"

    print('Bot:', response)
    await update.message.reply_text(response)


def handle_response(text: str)->str:
	processed: str = text.lower()
	if 'run barry run' in processed:
		return 'FLASH....'
	elif 'hello' in processed:
		return 'Hyy'
	elif 'thank you' in processed:
		return 'Anytime'
	else:
		return 'I did not understand that'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
	message_type:str=update.message.chat.type
	text: str=update.message.text
	print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
	if message_type =='group':
		if BOT_USERNAME in text:
			new_text: str=text.replace(BOT_USERNAME,'').strip()
			response: str=handle_response(new_text)
		else:
			return
	else:
		response:str=handle_response(text)
	print('Bot:', response)
	await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
	print(f'Update{update} caused error {context.error}')
if __name__=='__main__':
	app=Application.builder().token(Token).build()
	app.add_handler(CommandHandler('start',start_command))
	app.add_handler(CommandHandler('help',help_command))
	app.add_handler(CommandHandler('run',custom_command))
	app.add_handler(MessageHandler(filters.TEXT,handle_message))
	app.add_error_handler(error)	
	print("Polling....")
	app.run_polling(poll_interval=3)
		
















