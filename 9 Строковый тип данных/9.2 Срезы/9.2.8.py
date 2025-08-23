# Две половинки
text = input()
print(text[len(text) // 2 + len(text) % 2 :] + text[: len(text) // 2 + len(text) % 2])
