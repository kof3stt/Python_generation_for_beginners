# Цифра 2
text = input()
f = "Цифр нет"
for c in text:
    if c in "0123456789":
        f = "Цифра"
print(f)
