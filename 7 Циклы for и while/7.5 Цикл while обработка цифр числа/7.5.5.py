# Вторая цифра
n = int(input())
while n >= 10:
    sec = n % 10
    n //= 10
print(sec)
