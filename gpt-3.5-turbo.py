import openai
import telebot
from settings import OPENAI_API_KEY, TOKEN_FOR_BOT_GPT

openai.api_key = OPENAI_API_KEY

bot = telebot.TeleBot(TOKEN_FOR_BOT_GPT)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я чат бот можете спросить, что угодно")

messeges = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
    ]

def update(messages, role, content):
    messages.append({'role': role, 'content': content})
    return messages

@bot.message_handler(content_types=['text'])
def echo_all(message):
    try:
        update(messeges, 'user', message.text)
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messeges
        )
        bot.reply_to(message, response.choices[0]['message']['content'])

    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка')
        print(e)

bot.polling(non_stop=True)