import telebot
from .settings import *
from .views import *

bot = telebot.TeleBot(TG_KEY)

def send_welcome(bot, message):
    bot.reply_to(message, "Введите ИНН и отправьте его мне. \n")

@bot.message_handler(commands=['start'])
def message_welcome(message):
    send_welcome(bot, message)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    results = {}

    bot.send_message(message.from_user.id, 'Ожидайте ответа.....')

    results = search_results(message.text)

    for key, val in results.items():
        bot.send_message(message.from_user.id, f'{key} - {val}')


