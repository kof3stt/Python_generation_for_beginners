# Численный треугольник 3 🌶️
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end="")
    for k in range(i, 1, -1):
        print(k - 1, end="")
    print("")
