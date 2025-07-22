# Необычное сравнение 📊
first, second = input().lower(), input().lower()
filtered_first = filtered_second = ""
for c in first:
    if c.isalpha():
        filtered_first += c
for c in second:
    if c.isalpha():
        filtered_second += c
if filtered_first == filtered_second:
    print("YES")
else:
    print("NO")
