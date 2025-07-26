# Корректный ip-адрес
flag = "ДА"
for num in input().split("."):
    if not (0 <= int(num) <= 255):
        flag = "НЕТ"
        break
print(flag)
