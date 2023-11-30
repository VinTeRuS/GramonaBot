from telegram.ext import Updater, MessageHandler, Filters
import re

def add_punctuation(update, context):
    text = update.message.text
    sentences = re.split(r'(?<=[.!?]) +', text)
    punctuated_text = ' '.join(sentence.capitalize() for sentence in sentences)
    context.bot.send_message(chat_id=update.effective_chat.id, text=punctuated_text)

def main():
    updater = Updater("6357078829:AAFlV7hOdAGaA0b_8GtGIYDLiN0eGj_LcKs", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, add_punctuation))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
