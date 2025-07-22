# Количество членов
counter = 0
text = input()
while text != "стоп" and text != "хватит" and text != "достаточно":
    counter += 1
    text = input()
print(counter)
