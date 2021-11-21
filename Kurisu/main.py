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
            info(message.chat.id)
        elif message.text == 'Проверить удачу':
            rand_0_100(message.chat.id)
        elif message.text == 'Список дел':
            todo_list(message.chat.id)
        else:
            unknown_text(message.chat.id)

@bot.message_handler(content_types=['text'])
def info(id):
    bot.send_message(id, 'К сожалению, сейчас я нахожусь на ранней стадии разработки, '
                         'и все, что я могу, это назвать случайное число '
                         'в диапазоне от 0 до 100😔')
    bot.send_message(id, 'Но скоро у меня появятся новые функции, '
                         'и со временем я научусь поддерживать с тобой диалог☺️')

@bot.message_handler(content_types=['text'])
def rand_0_100(id):
    frt = random.randint(0, 100)
    bot.send_message(id, str(frt))
    if frt >= 90:
        bot.send_message(id, 'Такой результат достоин похвалы\n'
                                          'Может сходишь в казино?😘')
    elif frt <= 10:
        bot.send_message(id, 'Ничего страшного, в другой раз повезет больше😊')

@bot.message_handler(content_types=['text'])
def todo_list(id):
    bot.send_message(id, 'Сначала добавь мне эту функцию, бака😡')

@bot.message_handler(content_types=['text'])
def unknown_text(id):
    bot.send_message(id, 'Если бы я еще могла понять речь человека...')

print('Программа запущена')

bot.polling(none_stop=True)
