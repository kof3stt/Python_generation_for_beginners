# Наименьшее из четырёх чисел 🌶️
a, b, c, d = int(input()), int(input()), int(input()), int(input())
min_num = a
if b <= a:
    min_num = b
if c <= b:
    min_num = c
if d <= c:
    min_num = d
print(min_num)
