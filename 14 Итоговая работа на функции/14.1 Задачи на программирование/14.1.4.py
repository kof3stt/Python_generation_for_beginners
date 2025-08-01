# Число словами 🌶️
# объявление функции
def number_to_words(num):
    s = [
        "один",
        "два",
        "три",
        "четыре",
        "пять",
        "шесть",
        "семь",
        "восемь",
        "девять",
        "десять",
        "одиннадцать",
        "двенадцать",
        "тринадцать",
        "четырнадцать",
        "пятнадцать",
        "шестнадцать",
        "семнадцать",
        "восемнадцать",
        "девятнадцать",
        "двадцать",
        "тридцать",
        "сорок",
        "пятьдесят",
        "шестьдесят",
        "семьдесят",
        "восемьдесят",
        "девяносто",
        "",
    ]
    if num <= 20:
        return s[num - 1]
    else:
        return s[num // 10 - 1 + 18] + " " + s[num % 10 - 1]


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
