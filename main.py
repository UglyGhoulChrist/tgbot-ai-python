import re
from dotenv import load_dotenv
import os
import telebot

# Загрузка переменных среды из файла .env
load_dotenv()

# Получение токена
TOKEN = os.getenv('SECRET_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот, созданный в целях обучения. Напиши /help, чтобы получить список команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    response_text = (
        "/start - начать общение с ботом\n"
        "/help - получить список доступных команд\n"
        "/reverse - перевернуть текст после команды\n"
        "/upper - преобразовывать текст в верхний регистр\n"
        "/cut - удаляет гласные буквы\n"
        "/factorial - вычисляет факториал введённого числа\n"
        "Это всё, что я умею на данный момент!"
    )
    bot.reply_to(message, response_text)

@bot.message_handler(commands=['reverse'])
def reverse_text(message):
    try:
        # Извлекаем аргументы после команды /reverse (если они есть)
        text_to_reverse = message.text.split(' ', 1)[1]
        # Переворачиваем текст
        reversed_text = text_to_reverse[::-1]
        # Отправляем результат обратно пользователю
        bot.reply_to(message, reversed_text)
    except IndexError:
        # Если аргументов нет, отправляем сообщение об ошибке
         bot.reply_to(message, "Пожалуйста, отправьте текст после команды /reverse.")

@bot.message_handler(commands=['upper'])
def upper_text(message):
    try:
        # Извлекаем аргументы после команды /upper (если они есть)
        text_to_upper = message.text.split(' ', 1)[1]
        # Преобразуем текст
        upper_text = text_to_upper.upper()
        # Отправляем результат обратно пользователю
        bot.reply_to(message, upper_text)
    except IndexError:
        # Если аргументов нет, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, отправьте текст после команды /upper.")

@bot.message_handler(commands=['cut'])
def cut_text(message):
    try:
        # Извлекаем аргументы после команды /cut (если они есть)
        text_to_cut = message.text.split(' ', 1)[1]

        # Регулярное выражение для нахождения гласных
        vowels_pattern = re.compile(r'[aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ]', re.IGNORECASE)
        # Заменяем все найденные гласные на пустую строку
        result_text = vowels_pattern.sub('', text_to_cut)

        # Отправляем результат обратно пользователю
        bot.reply_to(message, result_text)
    except IndexError:
        # Если аргументов нет, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, отправьте текст после команды /cut.")

@bot.message_handler(commands=['factorial'])
def factorial_text(message):
    try:
        # Извлекаем аргументы после команды /factorial (если они есть)
        text_to_factorial = message.text.split(' ', 1)[1]

        number = int(text_to_factorial)

        if number<1:
            raise Exception

        result = 1
        for i in range(2, number + 1):  # Итерация от 2 до n включительно
            result *= i  # Умножение result на текущее значение i

        # Отправляем результат обратно пользователю
        bot.reply_to(message, result)
    except IndexError:
        # Если аргументов нет, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, напишите число после команды /factorial.")
    except Exception:
        # Если аргументов нет, отправляем сообщение об ошибке
        bot.reply_to(message, "Что-то пошло не так...")

# Запускаем бота, чтобы он постоянно ожидал входящие сообщения
bot.polling(none_stop=True)