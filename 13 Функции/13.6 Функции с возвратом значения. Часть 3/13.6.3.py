# Корни уравнения 🌶️
# объявление функции
from math import sqrt


def solve(a, b, c):
    D = b**2 - 4 * a * c
    if D == 0:
        return -b / (2 * a), -b / (2 * a)
    elif D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())


# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
