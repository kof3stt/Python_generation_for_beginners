# Шифр Цезаря 🌶️
n = int(input())
message = input()
for c in message:
    k = ord(c) - n
    if k < 97:
        k = k + 26
    print(chr(k), end="")
