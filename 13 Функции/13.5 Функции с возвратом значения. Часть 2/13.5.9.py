# Змеиный регистр 🐍
# объявление функции
def convert_to_python_case(text):
    c = ""
    for i in range(len(txt)):
        if txt[i].isupper():
            c = c + "_" + txt[i].lower()
        if txt[i].islower():
            c = c + txt[i]
        if txt[i].isdigit():
            c = c + txt[i]
    return c[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
