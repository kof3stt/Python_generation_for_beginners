# Красивое число 🌸🌶️
x = int(input())
if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")
