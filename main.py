# telegram-bot
import telebot
from time import sleep
from datetime import datetime
from telebot import types

bot = telebot.TeleBot('6881456125:AAGoHSFy41zOugswPzuhp8J7gUX1XwTm9-w')


def init():
    try:
        print('Bot status:START', datetime.now())
        bot.polling(none_stop=True)
    except Exception as e:
        print('Polling Error:', e)
        bot.stop_polling()
        print('Bot status: STOP', datetime.now())
        sleep(2)
        init()


@bot.message_handler(commands=['start'])
def start_handler(message):
    file = open('C:/Users/user/Desktop/b8839e0c5f9e01f8f2bcaef2c85531e7.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    print('id =', message.from_user.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("✏️Магазин", callback_data="edit")
    markup.add(btn1)
    bot.send_message(message.chat.id, '<b> Здравствуйте, это бот магазина рыболовных удилищ. </b>  \n',
                     reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call, self=None):
    if call.data == 'edit':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Фидерные удилища", callback_data='Feeder')
        btn2 = types.InlineKeyboardButton("Спиннинговые удилища", callback_data='Spinning')
        btn3 = types.InlineKeyboardButton("Поплавочные удилища", callback_data='Float_rods')
        btn4 = types.InlineKeyboardButton("В главное меню", callback_data='back_to_main_page')
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите виды удилищ:",
                              reply_markup=markup, parse_mode='html')
    elif call.data == 'back_to_main_page':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("✏️Магазин", callback_data='edit')
        markup.add(btn1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Здравствуйте, это бот магазина рыболовных удилищ",
                              reply_markup=markup, parse_mode='html')
    elif call.data == 'Feeder':
        file = open('photo/feeder_1.png', 'rb')
        bot.send_photo(call.data.chat.id, file)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее", callback_data='Further')
        btn7 = types.InlineKeyboardButton("Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("Купить", callback_data='buy')
        btn4 = types.InlineKeyboardButton("Назад в главное меню", callback_data='back_to_main_page')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Здравствуйте, это бот магазина рыболовных удилищ",
                              reply_markup=markup, parse_mode='html')
    elif call.data == 'Spinning':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее", callback_data='Further')
        btn7 = types.InlineKeyboardButton("Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("Купить", callback_data='buy')
        btn4 = types.InlineKeyboardButton("Назад в главное меню", callback_data='back_to_main_page')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Здравствуйте, это бот магазина рыболовных удилищ",
                              reply_markup=markup, parse_mode='html')
    elif call.data == 'Float_rods':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn6 = types.InlineKeyboardButton("Далее", callback_data='Further')
        btn7 = types.InlineKeyboardButton("Назад", callback_data='back')
        btn1 = types.InlineKeyboardButton("Купить", callback_data='buy')
        btn4 = types.InlineKeyboardButton("Назад в главное меню", callback_data='back_to_main_page')
        markup.row(btn7, btn6)
        markup.add(btn1, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Здравствуйте, это бот магазина рыболовных удилищ",
                              reply_markup=markup, parse_mode='html')


if __name__ == '__main__':
    init()
