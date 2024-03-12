numbers = [512, 124, 237, 19, 78, 345, 231]

for number in numbers:
    if number == 237:
        print("Остановка цикла при встрече числа 237")
        break  # Останавливаем цикл
    if number % 2 == 0:
        print(number)  # Вывод четного числа