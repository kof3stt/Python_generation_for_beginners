# Магические даты ✨
# объявление функции
def is_magic(date):
    return True if int(date[0]) * int(date[1]) == int(date[2][2:]) else False


# считываем данные
date = input().split(".")

# вызываем функцию
print(is_magic(date))
