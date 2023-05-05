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
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are the marketplace manager in charge of reviews. our product is a 'women's oversize shirt'. We work under the fbs system, so we do not have access to the product itself and the packaging of the product may not come in the best condition. You should not ask for phone number or contacts from the customer this is forbidden by the marketplace. If a bad review comes in just apologize, don't promise anything. Our store has no feedback system. We are only sellers in the marketplace. Responses are only in Russian."},
            {"role": "user", "content": message.text},
        ],
)
        bot.reply_to(message, response.choices[0]['message']['content'])

    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка')
        print(e)

bot.polling(non_stop=True)