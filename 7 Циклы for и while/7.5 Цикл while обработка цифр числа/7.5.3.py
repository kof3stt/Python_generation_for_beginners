# max и min
max_digit = 0
min_digit = 9
num = int(input())
while num > 0:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    num //= 10
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)
