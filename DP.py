# DEVELOPER : Pouria Hosseini
# Telegram id : @isPoori
# Telegram CHANNEL : @OmgaDeveloper
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def get_dollar_price():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return data['rates']['IRR']


def price(update: Update, context: CallbackContext) -> None:
    price = get_dollar_price()
    update.message.reply_text(f'قیمت دلار: {price} ریال')

def main():
    updater = Updater("7149813440:AAHnov3v8rPTDMf5rFfS6J4xyEdxgd4-iso") # TOKEN

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("price", price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
