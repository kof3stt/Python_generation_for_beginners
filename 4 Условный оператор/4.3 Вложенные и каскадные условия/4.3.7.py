# Цветовой микшер 🎨🌶️
first_col, second_col = input(), input()
if first_col == "красный":
    if second_col == "синий":
        print("фиолетовый")
    elif second_col == "желтый":
        print("оранжевый")
    elif second_col == "красный":
        print("красный")
    else:
        print("ошибка цвета")
elif first_col == "синий":
    if second_col == "красный":
        print("фиолетовый")
    elif second_col == "желтый":
        print("зеленый")
    elif second_col == "синий":
        print("синий")
    else:
        print("ошибка цвета")
elif first_col == "желтый":
    if second_col == "красный":
        print("оранжевый")
    elif second_col == "синий":
        print("зеленый")
    elif second_col == "желтый":
        print("желтый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")
