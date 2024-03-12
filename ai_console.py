from openai import OpenAI
from dotenv import load_dotenv
import os

# Загрузка переменных среды из файла .env
load_dotenv()

# Получение ключа
PROXY_API_KEY = os.getenv('SECRET_PROXY_API_KEY')

# Создание клиента для OpenAI с указанием API ключа и базового URL
client = OpenAI(
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Сообщения для инициализации диалога (если необходимо)
messages = []

# Цикл для ввода запросов пользователем и получения ответов от нейросети
while True:
    # Получение строки ввода от пользователя
    user_input = input("Вы: ")

    # Добавление запроса пользователя в список сообщений
    messages.append({"role": "user", "content": user_input})

    # Создание запроса на получение ответа от нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    # Получение и вывод ответа нейросети
    ai_response = chat_completion.choices[0].message.content
    print("AI: ", ai_response)

    # Добавление ответа нейросети в список сообщений для контекста
    messages.append({"role": "assistant", "content": ai_response})

    # Опционально добавьте условие выхода из цикла, например, если пользователь ввел "exit" или "quit"
    if user_input.lower() in ["exit", "quit"]:
        break