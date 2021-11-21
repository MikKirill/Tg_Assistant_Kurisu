import configs
import random
import telebot
from telebot import types
import data # Получаем нашу "базу данных"
from time import sleep

bot =telebot.TeleBot(configs.TOKEN)
text_list = ''

print('Запуск...')
    # Отображаем нашу базу
print(data.my_file.read())
sleep(1)

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

def info(id):
    bot.send_message(id, 'К сожалению, сейчас я нахожусь на ранней стадии разработки, '
                         'и все, что я могу, это назвать случайное число '
                         'в диапазоне от 0 до 100😔')
    bot.send_message(id, 'Но скоро у меня появятся новые функции, '
                         'и со временем я научусь поддерживать с тобой диалог☺️')

def rand_0_100(id):
    frt = random.randint(0, 100)
    bot.send_message(id, str(frt))
    if frt >= 90:
        bot.send_message(id, 'Такой результат достоин похвалы\n'
                                          'Может сходишь в казино?😘')
    elif frt <= 10:
        bot.send_message(id, 'Ничего страшного, в другой раз повезет больше😊')

def todo_list(id):
    bot.send_message(id, 'Вот тебе тестовой список😠')
        # Начало экспериментов с массивами
    demo_tasks(id)
    msg = bot.send_message(id, "Введи что-нибудь...\nИли не вводи\nВсе равно запишу🥱")
        # Ожидаем ввода и автоматически уходим в отдельную функцию...
    bot.register_next_step_handler(msg, new_demo_task)

def new_demo_task(message):
    id = message.chat.id
    data.TASKS.append(message.text) # Добавление в конец массива нового пункта
    bot.send_message(id, 'Я же сказала, что добавлю')
    bot.send_message(id, 'Вот, проверяй')
    demo_tasks(id)
    return

    # Отображение демонстрационного массива
def demo_tasks(id):
    global text_list
    c = 0
    for i in data.TASKS:
        c += 1
        text_list = (text_list + '\n' + str(c) + '. ' + i)
    bot.send_message(id, text_list)
    text_list = ''

def unknown_text(id):
    bot.send_message(id, 'Если бы я еще могла понять речь человека...')

print('Программа запущена')

bot.polling(none_stop=True)
