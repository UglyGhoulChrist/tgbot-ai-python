from fractions import Fraction

# Вещественное число, которое нужно преобразовать в дробь
number = 14.375

# Создание обыкновенной дроби из вещественного числа
fraction = Fraction(number).limit_denominator()

# Вывод результата
print(f"{number} = {fraction.numerator}/{fraction.denominator}")