# Самый частотный символ
text = input()
most_common = text[0]
for c in text:
    if text.count(c) >= text.count(most_common):
        most_common = c
print(most_common)
