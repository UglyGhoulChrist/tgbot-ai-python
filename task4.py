# Запрашиваем у пользователя количество секунд
user_input = input("Введите количество секунд: ")

# Проверяем, что введено целое число
try:
    total_seconds = int(user_input)
except ValueError:
    print("Пожалуйста, введите целое число.")
else:
    # Вычисляем дни, часы, минуты и секунды
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Выводим результат в формате дни:часы:минуты:секунды
    print(f"{days} дней : {hours} часов : {minutes} минут : {seconds} секунд")