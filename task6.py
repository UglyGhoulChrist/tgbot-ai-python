# Функция для выполнения арифметических операций
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: Деление на ноль невозможно"
        return num1 / num2
    else:
        return "Ошибка: Неизвестная операция"

# Запрашиваем у пользователя числа и операцию
try:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    # Выполнение операции и вывод результата
    result = calculate(number1, number2, operation)
    print(f"Результат: {result}")

except ValueError:
    print("Ошибка: Введите корректное число.")