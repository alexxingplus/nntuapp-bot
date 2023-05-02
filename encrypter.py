import logging
import telegram
from datetime import date
from telegram.base import TelegramObject
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InputMediaPhoto)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

token = 'PASTE YOUR TOKEN HERE'
ABC = '-1234567890СДЧЖИЭЫЬВТЕЁЪЦКЩФЗАГЯЛЙОШУБПМРХНЮСДЧЖИЭЫЬВТЕЁЪЦКЩФЗАГЯЛЙОШУБПМРХНЮ';

catBot = telegram.Bot(token)

def encrypt(input):
    tempString = input.replace(' ', '-').upper()
    if (input == ''):
        return ''
    now = date.today()
    today = int(now.strftime('%d'))
    output = ''
    for symbol in tempString:
        try:
            index = ABC.index(symbol)
            output += ABC[index + today]
        except:
            output += symbol
    return output

def echo(update, context):
    id = update.message.chat_id
    print("Cообщение: '{}' от {}, время: {}".format(update.message.text, id, update.message.date))
    update.message.reply_text(encrypt(update.message.text))
    
def error (update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text("Произошла ошибка, сообщите об этом разработчику (контакт есть в информации о боте)")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text | Filters.photo, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
