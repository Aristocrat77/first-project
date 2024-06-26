# telegram-bot
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
    connect = sqlite3.connect('database.db')
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
    file = open('photo/main_photo.jpg', 'rb')
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
        file = open('photo/main_photo.jpg', 'rb')
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
        file = open('photo/feeder_1.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file)
        with sqlite3.connect('db/database.db') as db:
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
        file = open('photo/Spinning_1.webp', 'rb')
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
        file = open('photo/Float_rods_1.webp', 'rb')
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


if __name__ == '__main__':
    init()
