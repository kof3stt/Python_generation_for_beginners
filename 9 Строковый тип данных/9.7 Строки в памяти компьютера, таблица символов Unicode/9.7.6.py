# Накручиваем стоимость ответа ⬆️🌶️
message = input()
fake_letters_en = "eyopaxcETOPAHXCBM"
fake_letters_ru = "еуорахсЕТОРАНХСВМ"
old_cost = new_cost = 0
for c in message:
    old_cost += ord(c) * 3
for i in range(len(fake_letters_en)):
    message = message.replace(fake_letters_en[i], fake_letters_ru[i])
for c in message:
    new_cost += ord(c) * 3
print(f"Старая стоимость: {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")
