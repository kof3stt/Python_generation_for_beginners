# Количество дней
# объявление функции
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
