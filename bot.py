from datetime import time

import config
import telebot
import logging
import Telegram.API as API
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Во славу котикам!\n Напиши 'Котик', что бы начать:)")


@bot.message_handler(content_types=['text'])
def input_text(message):
    if message.text.lower() == 'котики' \
            or message.text.lower() == '/cat' \
            or message.text.lower() == '/cat@funnyc4tsbot' \
            or message.text.lower() == 'кот' \
            or message.text.lower() == 'котик' \
            or message.text.lower() == 'собака' \
            or message.text.lower() == 'собачка' \
            or message.text.lower() == 'пёс' \
            or message.text.lower() == 'кит' \
            or message.text.lower() == '🐱' \
            or message.text.lower() == '🐶':
        call_markup(message)


def call_markup(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Котика🐱", callback_data='cat')
    item2 = types.InlineKeyboardButton("Собачку🐶", callback_data='dog')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Какую картиночку ты хочешь?:)', reply_markup=markup)


def call_markup_count_heart(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    heart = types.InlineKeyboardButton('❤', callback_data='heart')
    markup.add(heart)
    bot.send_message(message.chat.id, 'Понравилось?:)', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'cat':
                bot.send_message(call.message.chat.id, API.CatsAPI())
                call_markup(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Ещё котика?)🐱',
                                      reply_markup=None)

            elif call.data == 'dog':
                bot.send_message(call.message.chat.id, API.DogsAPI())
                call_markup(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Ещё собачку?)🐶',
                                      reply_markup=None)
    except Exception as e:
        print(repr(e))


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(e)
        time.sleep(15)
