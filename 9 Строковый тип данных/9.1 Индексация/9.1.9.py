# Одинаковые соседи
text = input()
k = 0
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        k += 1
print(k)
