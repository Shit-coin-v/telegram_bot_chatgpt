import openai
import telebot
from settings import OPENAI_API_KEY, TOKEN_FOR_BOT_GPT

openai.api_key = OPENAI_API_KEY

bot = telebot.TeleBot(TOKEN_FOR_BOT_GPT)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я чат бот можете спросить, что угодно")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            promt=message.text,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.7,
        )

        bot.reply_to(message, response.choices[0].text)

    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка')
        print(e)

bot.polling(non_stop=True)