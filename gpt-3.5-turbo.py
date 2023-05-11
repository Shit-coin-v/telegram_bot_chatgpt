import openai
import telebot
from settings import OPENAI_API_KEY, TOKEN_FOR_BOT_GPT

openai.api_key = OPENAI_API_KEY

bot = telebot.TeleBot(TOKEN_FOR_BOT_GPT)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я чат бот можете спросить, что угодно")

messeges = [
    {"role": "system", "content": "Your job is to respond to customer feedback, in the marketplace wildberries. Our Product Women's Oversize Shirt."},
    {"role": "user", "content": "The color does not match, much darker."},
    {"role": "manager", "content": "I am sorry to hear that the color did not meet your expectations and was much darker. We will pass the information on to quality control"},
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