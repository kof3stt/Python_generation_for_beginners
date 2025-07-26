# Количество совпадающих пар
data = input().split()
total = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            total += 1
print(total)
