# telegram-bot
import re
import telebot
from time import sleep
from datetime import datetime
from telebot import types
import sqlite3
from db import connect


bot = telebot.TeleBot('6881456125:AAGoHSFy41zOugswPzuhp8J7gUX1XwTm9-w')


def init():
    try:
        print('Bot status: START', datetime.now())
        bot.polling(none_stop=True)
    except Exception as e:
        print('Polling Error:', e)
        bot.stop_polling()
        print('Bot status: STOP', datetime.now())
        sleep(2)
        init()


@bot.message_handler(commands=['start'])
def start_handler(message):
    connect = sqlite3.connect('../db/database.db')
    cursor = connect.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
    id INTEGER
    )""")
    connect.commit()
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    file = open('../photo/main_photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🎣Магазин", callback_data="shop")
    btn2 = types.InlineKeyboardButton("🗑Корзина", callback_data="basket")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b> Здравствуйте, это бот магазина рыболовных удилищ. </b>  \n',
                     reply_markup=markup, parse_mode='html')


#with sqlite3.connect('db/database.db') as db:
 #   cursor = db.cursor()
  #  query = """CREATE TABLE IF NOT EXISTS goods (id INTEGER, brand TEXT, description TEXT, photo BLOB) """
   # cursor.execute(query)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call, self=None):
    if call.data == 'shop':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Фидерные удилища", callback_data='Feeder')
        btn2 = types.InlineKeyboardButton("Спиннинговые удилища", callback_data='Spinning')
        btn3 = types.InlineKeyboardButton("Поплавочные удилища", callback_data='Float_rods')
        btn4 = types.InlineKeyboardButton("Назад", callback_data='back_to_main_page')
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите виды удилищ:",
                              reply_markup=markup, parse_mode='html')

    elif call.data == 'back_to_main_page':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('../photo/main_photo.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🎣Магазин", callback_data="shop")
        btn2 = types.InlineKeyboardButton("🗑Корзина", callback_data="basket")
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, '<b> Здравствуйте, это бот магазина рыболовных удилищ. </b>  \n',
                         reply_markup=markup, parse_mode='html')

    elif call.data == 'back1':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Фидерные удилища", callback_data='Feeder')
        btn2 = types.InlineKeyboardButton("Спиннинговые удилища", callback_data='Spinning')
        btn3 = types.InlineKeyboardButton("Поплавочные удилища", callback_data='Float_rods')
        btn4 = types.InlineKeyboardButton("Назад", callback_data='back_to_main_page')
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите виды удилищ:",
                              reply_markup=markup, parse_mode='html')

    elif call.data == 'Feeder':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('../photo/feeder_1.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file)
        with sqlite3.connect('../db/database.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT brand, description FROM feeder_db')
            message = cursor.fetchone()
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее➡️", callback_data='Further')
        btn7 = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("🗑Добавить в корзину", callback_data='buy')
        btn4 = types.InlineKeyboardButton("↪️Назад в главное меню", callback_data='back1')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Название: {message[0]} \n"
                              f"Описание: {message[1]}",
                         reply_markup=markup, parse_mode='html')

    elif call.data == 'Spinning':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('../photo/Spinning_1.webp', 'rb')
        bot.send_photo(call.message.chat.id, file)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее➡️", callback_data='Further')
        btn7 = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("🗑Добавить в корзину", callback_data='buy')
        btn4 = types.InlineKeyboardButton("↪️Назад в главное меню", callback_data='back1')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Тут должны быть описание удилища, характеристики и цена",
                         reply_markup=markup, parse_mode='html')

    elif call.data == 'Float_rods':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('../photo/Float_rods_1.webp', 'rb')
        bot.send_photo(call.message.chat.id, file)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее➡️", callback_data='Further')
        btn7 = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("🗑Добавить в корзину", callback_data='buy')
        btn4 = types.InlineKeyboardButton("↪️Назад в главное меню", callback_data='back1')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Тут должны быть описание удилища, характеристики и цена",
                         reply_markup=markup, parse_mode='html')

    elif call.data == 'buy':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите номер телефона",
                              reply_markup=None, parse_mode='html')

        bot.register_next_step_handler(send, check_phone_number)

    elif call.data == 'mail':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                     text="Введите mail",
                                     reply_markup=None, parse_mode='html')

        bot.register_next_step_handler(send, check_mail)


# Проверка номера телефона
def check_phone_number(message: dict):
    if message.content_type != "text":
        msg_back_or_repeat('back_to_main_page', 'buy', 'Похоже, Вы прислали не текст😕', message)
        return

    phone_num = message.text.lower()

    result_phone_num = ''

    for char in phone_num:
        if char.isdigit():
            result_phone_num += char

    if not result_phone_num:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data='back_to_main_page')
        btn2 = types.InlineKeyboardButton('Повторить ввод', callback_data='buy')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Номер телефона должен содержать только цифры", reply_markup=markup)
        return

    if not re.fullmatch(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', result_phone_num):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data='back_to_main_page')
        btn2 = types.InlineKeyboardButton('Повторить ввод', callback_data='buy')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, f"Неправильный формат номера телефона", reply_markup=markup)
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Ввести mail', callback_data='mail')
    markup.add(btn1)
    bot.send_message(message.chat.id, f"Готово, теперь введите свой mail", reply_markup=markup)


# Функция отправки сообщения с ошибкой ввода пользователя и кнопками назад / повторить
def msg_back_or_repeat(bt1: str, bt2: str, msg: str, message: dict) -> None:
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('◀️ Назад', callback_data=f'{bt1}')
    btn2 = types.InlineKeyboardButton('Повторить ввод', callback_data=f'{bt2}')
    markup.add(btn1, btn2)
    bot.edit_message_text(message.chat.id, f'{msg}', reply_markup=markup)


def check_mail(message: dict) -> None:
    if message.content_type != "text":
        msg_back_or_repeat('back_to_main_page', 'buy', 'Похоже, Вы прислали не текст😕', message)
        return

    mail = message.text.lower()
    print(mail)

    if not mail:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data='back_to_main_page')
        btn2 = types.InlineKeyboardButton('Повторить ввод', callback_data='buy')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "mail должен содержать только, буквы", reply_markup=markup)
        return

    if not re.fullmatch(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', mail):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data='back_to_main_page')
        btn2 = types.InlineKeyboardButton('Повторить ввод', callback_data='buy')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, f"Неправильный формат mail", reply_markup=markup)
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Оплатить💳', callback_data='pay')
    markup.add(btn1)
    bot.send_message(message.chat.id, f"Готово, теперь вы можете оплатить билет", reply_markup=markup)


if __name__ == '__main__':
    init()
