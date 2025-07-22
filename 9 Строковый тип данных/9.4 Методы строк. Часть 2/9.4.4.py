# Количество цифр
text = input()
cnt = 0
for i in range(10):
    cnt += text.count(str(i))
print(cnt)
