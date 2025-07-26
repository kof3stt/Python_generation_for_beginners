# Сортировка чисел
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
data.sort()
print(*data)
data.sort(reverse=True)
print(*data)
