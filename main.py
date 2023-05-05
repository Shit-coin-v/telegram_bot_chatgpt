import telebot
from telebot import types
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Изменить ответ', callback_data='edit')
    btn2 = types.InlineKeyboardButton('Отправить ответ', callback_data='edit')
    markup.add(btn1, btn2)
    bot.reply_to(message, 'Спасибо, что вы выбрали нас', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(non_stop=True) 