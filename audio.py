import telebot
from gtts import gTTS
from io import BytesIO
from dotenv import load_dotenv
import os

# Загрузка переменных среды из файла .env
load_dotenv()

# Получение токена бота и ключа для OpenAI
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
 
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который превращает текст в аудио. Просто отправь мне сообщение.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    tts = gTTS(text, lang='ru')
    voice = BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)  # Перемещаем указатель на начало файла
    
    bot.send_voice(chat_id=message.chat.id, voice=voice)

bot.polling()