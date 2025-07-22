# Последовательность чисел 2 🌶️
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
