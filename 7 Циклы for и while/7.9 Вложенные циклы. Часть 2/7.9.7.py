# Простые числа 👌
a, b = int(input()), int(input())
for i in range(a, b + 1):
    flag = False
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = True
    if not flag and i != 1:
        print(i)
