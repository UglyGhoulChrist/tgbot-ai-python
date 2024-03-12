# Функция для конвертации из Цельсия в Фаренгейты
def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

# Функция для конвертации из Фаренгейтов в Цельсии
def fahrenheit_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * 5/9

# Основная программа
if __name__ == "__main__":
    print("Конвертер температуры")
    print("1: Цельсий в Фаренгейт")
    print("2: Фаренгейт в Цельсий")
    
    # Запрашиваем у пользователя выбор направления конвертации
    choice = input("Выберите опцию (1 или 2): ")
    
    if choice == '1':
        # Конвертация из Цельсия в Фаренгейты
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Температура в градусах Фаренгейта: {fahrenheit:.2f}")
    elif choice == '2':
        # Конвертация из Фаренгейтов в Цельсии
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Температура в градусах Цельсия: {celsius:.2f}")
    else:
        print("Неправильный выбор. Пожалуйста, выберите 1 или 2.")