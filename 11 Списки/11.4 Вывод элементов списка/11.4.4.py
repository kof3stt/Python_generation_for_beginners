# Без дубликатов
my_list = []
for _ in range(int(input())):
    text = input()
    if text not in my_list:
        my_list.append(text)
print(*my_list, sep="\n")
