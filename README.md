# Введение в Python-разработку с помощью ChatGPT

## main.py - ТГ-бот

### Изолированное окружение:

1. mkdir myproject
   cd myproject

2. python -m venv env
   
3. env\Scripts\activate.bat (deactivate)

4. pip install package_name

5. pip freeze > requirements.txt

6. pip install -r requirements.txt

### Конфиденциальная информация:

1. pip install python-dotenv

2. Создайте в корне вашего проекта файл с названием `.env`.

3. В файле `.env` SECRET_TOKEN=ваш_секретный_токен

4. Добавьте файл `.env` в файл `.gitignore`

5. from dotenv import load_dotenv
   import os
   
   Загрузка переменных среды из файла .env
   load_dotenv()
   
   Получение токена
   secret_token = os.getenv('SECRET_TOKEN')
   
   Теперь можно использовать secret_token в вашем коде

### OpenAI

1. pip install openai