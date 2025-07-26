# Искомый месяц 📅
# объявление функции
def get_month(language, number):
    if lan == "en":
        en = [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]
        return en[num - 1]
    elif lan == "ru":
        ru = [
            "январь",
            "февраль",
            "март",
            "апрель",
            "май",
            "июнь",
            "июль",
            "август",
            "сентябрь",
            "октябрь",
            "ноябрь",
            "декабрь",
        ]
        return ru[num - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
