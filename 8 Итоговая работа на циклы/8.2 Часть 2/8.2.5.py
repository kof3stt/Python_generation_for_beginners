# Третья цифра 3️⃣
n = int(input())
last = 0
while n >= 100:
    last = n % 10
    n //= 10
print(last)
