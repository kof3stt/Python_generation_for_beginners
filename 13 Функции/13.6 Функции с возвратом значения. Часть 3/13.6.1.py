# Середина отрезка
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    return (x_1 + x_2) / 2, (y_1 + y_2) / 2


# считываем данные
x_1, y_1 = float(input()), float(input())
x_2, y_2 = float(input()), float(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
