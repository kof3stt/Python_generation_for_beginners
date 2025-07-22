# Правильный многоугольник 🔶
from math import tan, pi


n, a = int(input()), float(input())
print(n * a**2 / (4 * tan(pi / n)))
