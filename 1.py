elif call.data == 'back_to_main_page':
markup = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton("✏️Магазин", callback_data='edit')
markup.add(btn1)
bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Здравствуйте, это бот магазина рыболовных удилищ",
                      reply_markup=markup, parse_mode='html')