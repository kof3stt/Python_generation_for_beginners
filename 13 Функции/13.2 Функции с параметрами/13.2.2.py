# ФИО
# объявление функции
def print_fio(name, surname, patronymic):
    print((surname[0] + name[0] + patronymic[0]).upper())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
