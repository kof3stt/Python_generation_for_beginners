# Нижний регистр 🔽
text = input()
text_lower = text.upper()
counter = 0
for i in range(len(text)):
    if text[i] != text_lower[i] and text[i] not in "0123456789":
        counter += 1
print(counter)
