# Сколько раз?
total_plus, total_star = 0, 0
text = input()
for c in text:
    if c == "+":
        total_plus += 1
    elif c == "*":
        total_star += 1
print("Символ + встречается", total_plus, "раз")
print("Символ * встречается", total_star, "раз")
