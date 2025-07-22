# Очень странные дела 📻
counter = 0
for i in range(int(input())):
    text = input()
    if text.count("11") >= 3:
        counter += 1
print(counter)
