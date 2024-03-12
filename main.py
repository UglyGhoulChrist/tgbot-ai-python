from dotenv import load_dotenv
import os
import telebot

# Загрузка переменных среды из файла .env
load_dotenv()

# Получение токена
TOKEN = os.getenv('SECRET_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой телеграм бот. Чем могу помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "привет" in text:
        bot.reply_to(message, "Привет, рад тебя видеть!")
    elif "как дела?" in text:
        bot.reply_to(message, "Всё отлично, спасибо!")
    else:
        bot.reply_to(message, f"Пока я повторюшка: {text}" )

bot.polling(none_stop=True)