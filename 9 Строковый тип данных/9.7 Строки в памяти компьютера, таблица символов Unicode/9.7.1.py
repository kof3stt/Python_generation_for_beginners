# Какая следующая буква? 🔜
letter = input()
if letter != "Я":
    print(chr(ord(letter) + 1))
else:
    print("Дальше букв нет")
