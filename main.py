from openai import OpenAI
from dotenv import load_dotenv
import os
import telebot

# Загрузка переменных среды из файла .env
load_dotenv()

# Получение токена бота и ключа для OpenAI
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PROXY_API_KEY = os.getenv('SECRET_PROXY_API_KEY')

# Создание клиента для OpenAI с указанием API ключа и базового URL
client = OpenAI(
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Сообщения для инициализации диалога (если необходимо)
messages = []

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может отвечать на твои вопросы. Напиши что-нибудь.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получение текста сообщения от пользователя
    user_input = message.text

    # Добавление запроса пользователя в список сообщений
    messages.append({"role": "user", "content": user_input})

    # Создание запроса на получение ответа от нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    # Получение и вывод ответа нейросети
    response_message = chat_completion.choices[0].message.content

    # Отправка ответа пользователю в чат
    bot.reply_to(message, response_message)

    # Добавление ответа нейросети в список сообщений для контекста
    messages.append({"role": "system", "content": response_message})
    # messages.append({"role": "system", "content": "отвечай в стилистике весёлого клоуна"})

bot.polling(none_stop=True)