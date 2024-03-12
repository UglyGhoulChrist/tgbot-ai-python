import random

# Запрос интервала у пользователя
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

# Генерация случайного числа
random_number = random.randint(min_value, max_value)

# Вывод случайного числа на экран
print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")