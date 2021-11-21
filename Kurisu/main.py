import configs
import random
import telebot
from telebot import types

bot =telebot.TeleBot(configs.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_pic = open(configs.WELCOME_IMG, 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Что ты можешь?')
    item2 = types.KeyboardButton('Проверить удачу')
    item3 = types.KeyboardButton('Список дел')

    markup.add(item1, item2, item3)

    bot.send_photo(message.chat.id, welcome_pic)
    bot.send_message(message.chat.id, 'Привет, мой дорогой друг!')
    bot.send_message(message.chat.id, "Меня зовут Курису Макисэ\nЯ твой бот-ассистент")
    bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def ma_in(message):
    if message.chat.type == 'private':
        if message.text == 'Что ты можешь?':
            bot.send_message(message.chat.id, 'К сожалению, сейчас я нахожусь на ранней стадии разработки, '
                                              'и все, что я могу, это назвать случайное число '
                                              'в диапазоне от 0 до 100😔')
            bot.send_message(message.chat.id, 'Но скоро у меня появятся новые функции, '
                                              'и со временем я научусь поддерживать с тобой диалог☺️')
        elif message.text == 'Проверить удачу':
            frt = random.randint(0, 100)
            bot.send_message(message.chat.id, str(frt))
            if frt >= 90:
                bot.send_message(message.chat.id, 'Такой результат достоин похвалы\n'
                                                  'Может сходишь в казино?😘')
            elif frt <= 10:
                bot.send_message(message.chat.id, 'Ничего страшного, в другой раз повезет больше😊')
        elif message.text == 'Список дел':
            bot.send_message(message.chat.id, 'Сначала добавь мне эту функцию, бака😡')

bot.polling(none_stop=True)
