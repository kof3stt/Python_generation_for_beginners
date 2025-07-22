# Упорядоченные цифры 🌶️
num = int(input())
flag = "YES"
last_digit = num % 10
num //= 10
while num > 0:
    current_digit = num % 10
    if current_digit < last_digit:
        flag = "NO"
    last_digit = current_digit
    num //= 10
print(flag)
