# Стоимость ответа 💬
text = input()
cost = 0
for c in text:
    cost += ord(c) * 3
print(f"Текст сообщения: '{text}'")
print(f"Стоимость сообщения: {cost}🐝")
